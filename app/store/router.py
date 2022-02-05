from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlmodel import Session, select

from database.session import get_session
from app.store.models import StoreRead, Store
# from app.store.service import Service


router = APIRouter()


# @router.get("", response_model=List[StoreRead], status_code=status.HTTP_200_OK)
# def read_store(session: Session = Depends(get_session)):
#     return Service.find_all(session)


@router.get("", response_model=List[StoreRead])
def read_stores(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    stores = session.exec(select(Store).offset(offset).limit(limit)).all()
    return stores
