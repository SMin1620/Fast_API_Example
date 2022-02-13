from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Any
from sqlmodel import Session, select

from database.session import get_session
from app.store.models import StoreRead, Store, StoreCreate
from app.store.exceptions import StoreNotFoundException
from app.store.service import service

router = APIRouter()


# @router.get("", response_model=List[StoreRead], status_code=status.HTTP_200_OK)
# def read_store(session: Session = Depends(get_session)):
#     return Service.find_all(session)


# @router.get("", response_model=List[StoreRead], status_code=status.HTTP_200_OK)
# def read_stores(
#     *,
#     session: Session = Depends(get_session),
#     offset: int = 0,
#     limit: int = Query(default=100, lte=100),
#     id: Any
# ):
#     stores = session.exec(select(Store).offset(offset).limit(limit)).all()
#     return stores

# test
@router.get("", response_model=List[StoreRead], status_code=status.HTTP_200_OK)
def read_stores(session: Session = Depends(get_session)):
    return service.find_all(session)


# ANCHOR: board document 조회
@router.get("/{store_id}", response_model=StoreRead, status_code=status.HTTP_200_OK)
def read_board(
    *,
    session: Session = Depends(get_session),
    store_id: int,
):
    store = service.find_one(session, store_id)
    if not store:
        raise StoreNotFoundException()

    return store


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

