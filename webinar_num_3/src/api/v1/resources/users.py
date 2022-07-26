from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from src.api.v1.schemas import CreatedUser, AuthUser
from src.services import UserService, get_user_service

from pydantic import EmailStr

router = APIRouter()

@router.post(path="/",
    response_model=CreatedUser,
    summary="Создать аккаунт",
    tags=["users"],
)
def create_user(
        user:CreatedUser, user_service: UserService = Depends(get_user_service)
):
    user: dict = user_service.create_user(user=user)
    if not user:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="This user already exists")
    return CreatedUser(**user)


@router.get (path="/",
    response_model= str,
    summary="Авторизация, выдача токенов",
    tags=["users"],
)
def login(name: str, password: str, user_service: UserService = Depends(get_user_service)
):
    token: str = user_service.authorize(name=name, password=password)
    if not token:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Username or password is invalid")
    return token

@router.get (path="/{get_user}/{user}",
    response_model=AuthUser,
    summary="Просмотр информации о пользователях",
    tags=["users"],
)
def view(token: str, user_service: UserService = Depends(get_user_service)
):
    user: dict = user_service.view_user(token=token)
    if not user:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Authorisation required")
    return AuthUser(**user)

@router.patch (path="/",
    response_model= str,
    summary="Изменение данных о пользователе",
    tags=["users"]
)
def change_user(token:str, new_email:str, new_password:str, user_service: UserService = Depends(get_user_service)
):
    token: str = user_service.change_user(token=token, new_email=new_email, new_password=new_password)
    if not token:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Authorisation required")
    return token

@router.get(path="/{user_id}",
    response_model=CreatedUser,
    summary="Выход",
    tags=["users"]
)
def logout(token:str, user_service: UserService = Depends(get_user_service)
):
    user: dict = user_service.logout(token=token)
    if not user:
        raise HTTPException(status_code=UNAUTHORIZED, detail="Authorisation required")
    return CreatedUser(**user)