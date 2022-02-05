from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlmodel import Session, select

from database.session import get_session
from app.menu.models import Menu, MenuRead


router = APIRouter()


@router.get("", response_model=List[MenuRead])
def read_stores(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    menus = session.exec(select(Menu).offset(offset).limit(limit)).all()
    return menus