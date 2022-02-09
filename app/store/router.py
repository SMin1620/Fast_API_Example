from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

from database.session import get_session
from app.store.models import StoreRead, Store, StoreCreate
from app.store.exceptions import StoreNotFoundException


router = APIRouter()


# @router.get("", response_model=List[StoreRead], status_code=status.HTTP_200_OK)
# def read_store(session: Session = Depends(get_session)):
#     return Service.find_all(session)


@router.get("", response_model=List[StoreRead], status_code=status.HTTP_200_OK)
def read_stores(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    stores = session.exec(select(Store).offset(offset).limit(limit)).all()
    return stores


# 상점 생성
@router.post("/create", response_model=StoreRead, status_code=status.HTTP_201_CREATED)
def create_store(
        *,
        session: Session = Depends(get_session),
        object_in: StoreCreate
):
    db_store = Store.from_orm(object_in)
    session.add(db_store)
    session.commit()
    session.refresh(db_store)
    return db_store

