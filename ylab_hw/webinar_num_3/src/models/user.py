from typing import Optional
from pydantic import EmailStr
#from src.models.token import Access_token, Refresh_token
from sqlmodel import Field, SQLModel

__all__ = ("User",)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    email: EmailStr = Field(nullable=False)
    password: str = Field(nullable=False)
    is_active: bool = Field(default=False)
    access_token: str = Field(default=None)
    refresh_token: str = Field(default=None)



