from typing import Optional
from sqlmodel import Field, SQLModel
from src.models.user import User

__all__ = ("Access_token","Refresh_token", "Blocked_tokens",)

class Access_token(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: int = Field(nullable=False, foreign_key=User.id)
    access_token: str = Field(nullable=False)

class Refresh_token(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: int = Field(nullable=False, foreign_key=User.id)
    refresh_token: str = Field(nullable=False)

class Blocked_tokens(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: int = Field(nullable=False, foreign_key=User.id)
    access_token: str = Field(nullable=False)
    refresh_token: str = Field(nullable=False)
