from typing import TYPE_CHECKING, List, Optional
from uuid import UUID
from pydantic import HttpUrl
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.store.models import Store


# 메뉴 모델
class Menu(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: Optional[str] = None
    price: Optional[int] = None
    menu_image: Optional[HttpUrl] = None

    store_id: Optional[int] = Field(default=None, foreign_key='store.id')
    store: Optional["Store"] = Relationship(back_populates='menu')


class MenuRead(SQLModel):
    id: int = Field(default=None, primary_key=True)
    name: Optional[str] = None
    price: Optional[int] = None
    menu_image: Optional[HttpUrl] = None
