from typing import TYPE_CHECKING, List, Optional
from uuid import UUID
from pydantic import HttpUrl
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.store.models import Store


# 메뉴 베이스
class MenuBase(SQLModel):
    name: str
    price: int

    store_id: Optional[int] = Field(default=None, foreign_key='store.id')


# 메뉴 모델
class Menu(MenuBase, table=True):
    id: int = Field(default=None, primary_key=True)

    store: Optional["Store"] = Relationship(back_populates='menu')


# 메뉴 조회
class MenuRead(SQLModel):
    id: int = Field(default=None, primary_key=True)

    store_id: int


# 메뉴 생성
class MenuCreate(MenuBase):
    pass
