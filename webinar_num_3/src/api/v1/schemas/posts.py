from datetime import datetime

from pydantic import BaseModel

__all__ = (
    "PostModel",
    "PostCreate",
    "PostListResponse",
)


class PostBase(BaseModel):
    title: str
    description: str


class PostCreate(PostBase):
    user: int


class PostModel(PostBase):
    id: int
    created_at: datetime


class PostListResponse(BaseModel):
    posts: list
# list[PostModel]
