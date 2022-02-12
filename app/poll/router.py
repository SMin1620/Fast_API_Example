from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlmodel import Session, select

from database.session import get_session
from app.poll.models import Poll, PollCreate, PollContent, PollRead
from app.poll.service import service


router = APIRouter()


@router.get("/", response_model=List[PollRead])
def read_poll(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    polls = session.exec(select(Poll).offset(offset).limit(limit)).all()
    return polls


# @router.post("/", response_model=PollCreate, status_code=status.HTTP_200_OK)
# def create_poll

