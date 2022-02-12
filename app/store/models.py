from typing import Optional, List, TYPE_CHECKING, Any
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.menu.models import Menu, MenuRead
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
class StoreRead(StoreBase):
    id: int
    name: str
    address: str

    poll: Any


class StoreReadWithMenu(StoreRead):
    menus: List["MenuRead"] = []


# 상점 생성
class StoreCreate(StoreBase):
    pass


# 상점 수정
class StoreUpdate(SQLModel):
    pass


