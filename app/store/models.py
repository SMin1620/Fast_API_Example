from typing import Optional, List, TYPE_CHECKING, Any
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship


# 상점 모델
class Article(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=50)
    content: str = Field(max_length=150)


class ArticleCreate(Article):
    pass


class ArticleUpdate(Article):
    pass

