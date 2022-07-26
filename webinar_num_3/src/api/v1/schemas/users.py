from pydantic import BaseModel, EmailStr

__all__ = (
    "UserModel",
    "CreatedUser",
    "AuthUser",
)

class UserModel(BaseModel):
    name: str
    email: EmailStr
    password: str

class CreatedUser(UserModel):
    id: int

class AuthUser(UserModel):
    is_active: bool
    access_token: str