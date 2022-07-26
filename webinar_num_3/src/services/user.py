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
from src.models import User
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

    def authorize(self, name: str, password: str):
        """Авторизация пользователя, выдача токенов"""
        user = self.session.query(User).filter(User.name == name).first()
        if user:
            if self.validate_password(password, user.password):
                user.is_active = True
                refresh = self.get_tokens(user)
                return f'refresh token: {refresh}' if user else None

    def get_tokens(self, user: AuthUser):
        """Выдача токенов"""
        user.access_token = self.create_access_token(user.name)
        refresh_token = self.create_refresh_token(user.name)
        self.session.commit()
        self.session.refresh(user)
        self.cache.set(key=f'{user.id}', value=f'{refresh_token}', expire=REFRESH_TOKEN_EXPIRE_MINUTES)
        self.cache.select(3)
        self.cache.set(key=f'{refresh_token}', value=f'{user.json()}', expire=REFRESH_TOKEN_EXPIRE_MINUTES)
        self.cache.select(0)
        return refresh_token

    def view_user(self, token: str):
        """Получение данных о пользователе"""
        self.cache.select(3)
        if user := self.cache.get(key=f'{token}'):
            cur_user = json.loads(user)
            self.cache.select(0)
            return cur_user
        else:
            self.cache.select(0)
            return None

    def change_user(self, token: str, new_email: EmailStr, new_password: str):
        """Смена данных о пользователе"""
        self.cache.select(3)
        if user := self.cache.get(key=f'{token}'):
            my_user = json.loads(user)
            cur_user = self.session.query(User).filter(User.id == my_user['id']).first()
            self.cache.delete(key=f'{token}')
            self.cache.select(1)
            self.cache.set(key=f'{token}', value=cur_user.json())
            self.cache.select(0)
            self.cache.delete(key=f'{cur_user.id}')
            cur_user.email = new_email
            cur_user.password = self.hash_password(new_password)
            refresh = self.get_tokens(cur_user)
            return f'refresh token: {refresh}'
        else:
            self.cache.select(0)
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
        self.cache.select(3)
        if user := self.cache.get(key=f'{token}'):
            cur_user = json.loads(user)
            my_user = self.session.query(User).filter(User.id == cur_user['id']).first()
            self.cache.delete(key=f'{token}')
            self.cache.select(1)
            self.cache.set(key=f'{token}', value=my_user.json())
            self.cache.select(0)
            self.cache.delete(key=f'{my_user.id}')
            my_user.is_active = False
            my_user.access_token = None
            self.session.commit()
            self.session.refresh(my_user)
            return my_user.dict()
        else:
            self.cache.select(0)
            return None



# get_user_service — это провайдер UserService. Синглтон
@lru_cache()
def get_user_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> UserService:
    return UserService(cache=cache, session=session)
