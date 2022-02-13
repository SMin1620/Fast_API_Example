from typing import Optional, List, TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.store.models import Store


# 투표
# class PollVote(SQLModel):
#     poll_id: Optional[int] = Field(foreign_key="poll.id", default=None)
#     poll: Optional["Poll"] = Relationship(back_populates="vote")
#
#     content_id: Optional[str] = Field(foreign_key="pollcontent.id", default=None)
#     content: Optional["PollContent"] = Relationship(back_populates="vote")


# 투표 내용
class PollContent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    content: str = Field(max_length=200, nullable=False)

    # store_id: Optional[int] = Field(default=None, foreign_key="store.id")
    # store: Optional["Store"] = Relationship(back_populates="content")
    poll_id: Optional[int] = Field(foreign_key="poll.id", default=False)
    poll: Optional["Poll"] = Relationship(back_populates="contents")


# 투표 모델
class Poll(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str

    contents: List["PollContent"] = Relationship(back_populates="poll")
    # vote: Optional["PollVote"] = Relationship(back_populates="poll")


# 투표 생성
class PollCreate(SQLModel):
    title: str
    contents: List[str] = []


# 투료 목록
class PollRead(SQLModel):
    id: int
    title: str
    contents: List[str] = []






