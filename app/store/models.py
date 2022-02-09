from typing import Optional, List, TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.menu.models import Menu
    # from app.poll.models import PollSelect


class StoreBase(SQLModel):
    name: str = Field(max_length=100)
    address: str
    opening: Optional[str] = None
    tags: Optional[str] = None
    tel_number: Optional[str] = None

    naver_score: Optional[float] = None
    daum_score: Optional[float] = None


# 상점 모델
class Store(StoreBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    menu: List['Menu'] = Relationship(back_populates='store')
    # select: Optional['PollSelect'] = Relationship(back_populates='store')


# 상점 조회 모델
class StoreRead(SQLModel):
    id: int
    name: str
    address: str


# 상점 생성
class StoreCreate(StoreBase):
    pass


