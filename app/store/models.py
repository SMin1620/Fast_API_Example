from typing import Optional, List, TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.menu.models import Menu


# 상점 모델
class Store(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name = str
    address: str
    opening: Optional[str] = None
    tags: Optional[str] = None
    tel_number: Optional[str] = None

    naver_score: Optional[float] = None
    daum_score: Optional[float] = None

    menu: List['Menu'] = Relationship(back_populates='store')


# 상점 조회 모델
class StoreRead(SQLModel):
    id: int
    name: str
    address: str



