from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlmodel import Session, select

from database.session import get_session
from app.menu.models import Menu, MenuRead, MenuCreate


router = APIRouter()


# 메뉴 조회
@router.get("", response_model=List[MenuRead])
def read_stores(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    menus = session.exec(select(Menu).offset(offset).limit(limit)).all()
    return menus


# 메뉴 생성
@router.post("", response_model=MenuRead)
def create_menu(
        *,
        session: Session = Depends(get_session),
        object_in: MenuCreate
):
    db_menu = Menu.from_orm(object_in)
    session.add(db_menu)
    session.commit()
    session.refresh(db_menu)
    return db_menu

