import json
from functools import lru_cache
from typing import Optional

import hashlib
import random
import string
from pydantic import EmailStr
from datetime import datetime, timedelta
from fastapi import Depends
from sqlmodel import Session

from src.api.v1.schemas import CreatedUser, AuthUser
from src.db import AbstractCache, get_cache, get_session
from src.models import User, Access_token, Refresh_token, Blocked_tokens
from src.services import ServiceMixin

import jwt

from src.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM

__all__ = ("UserService", "get_user_service")

class UserService(ServiceMixin):
    def check_user(self, user: CreatedUser):
        """Проверить, зарегистрирован ли пользователь в системе"""
        if any ((self.session.query(User).filter(User.email == user.email).first(),
            self.session.query(User).filter(User.name == user.name).first())):
            return None
        else:
            return True

    def create_user(self, user: CreatedUser) -> dict:
        """Зарегистрировать пользователя"""
        result = self.check_user(user)
        if result:
            hashed_password = self.hash_password(user.password)
            new_user = User(name=user.name, email=user.email, password=hashed_password)
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)
            return new_user.dict()
        else:
            return result

    def get_random_string(self, length=12):
        """ Генерирует случайную строку, использующуюся как соль """
        return "".join(random.choice(string.ascii_letters) for _ in range(length))

    def hash_password(self, password: str, salt: str = None):
        """ Хеширует пароль с солью """
        if salt is None:
            salt = self.get_random_string()
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def validate_password(self, user_password: str, hashed_password: str):
        """ Проверяет, что хеш пароля совпадает с хешем из БД """
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def authorize(self, email: EmailStr, password: str):
        """Авторизация пользователя, выдача токенов"""
        user = self.session.query(User).filter(User.email == email).first()
        if user:
            self.validate_password(password, user.password)
            self.cache.set(key=f"{user.email}", value=user.json())
            user.is_active = True
            self.get_tokens(user)
            return user.dict() if user else None

    def get_tokens(self, user: AuthUser):
        """Выдача токенов"""
        user.access_token = self.create_access_token(user.name)
        user.refresh_token = self.create_refresh_token(user.name)
        access_token = Access_token(user=user.id, access_token=user.access_token)
        refresh_token = Refresh_token(user=user.id, refresh_token=user.refresh_token)
        self.session.add(access_token)
        self.session.add(refresh_token)
        self.session.commit()
        self.session.refresh(user)
        self.session.refresh(access_token)
        self.session.refresh(refresh_token)
        return user.dict()

    def change_user(self, token: str, new_email: EmailStr, new_password: str):
        """Смена данных о пользователе"""
        user = self.session.query(User).filter(User.access_token == token).first()
        if token:
           user.email = new_email
           user.password = self.hash_password(new_password)
           self.get_tokens(user)
           return user.dict()
        else:
            return None

    def create_access_token(self, subject: str, expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
        return encoded_jwt


    def create_refresh_token(self, subject: str, expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
        return encoded_jwt

    def logout(self, token: str):
        user = self.session.query(User).filter(User.access_token == token).first()
        access_token = self.session.query(Access_token).filter(Access_token.user == user.id).first()
        refresh_token = self.session.query(Refresh_token).filter(Refresh_token.user == user.id).first()
        blocked = Blocked_tokens(user=user.id, access_token=access_token.access_token,refresh_token=refresh_token.refresh_token)
        del access_token
        del refresh_token
        user.is_active = False
        user.access_token = None
        user.refresh_token = None
        self.session.add(blocked)
        self.session.commit()
        self.session.refresh(user)
        self.session.refresh(blocked)
        return user.dict()



# get_user_service — это провайдер UserService. Синглтон
@lru_cache()
def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> UserService:
    return UserService(cache=cache, session=session)
