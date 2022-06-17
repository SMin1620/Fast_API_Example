from fastapi import APIRouter

from app.store.router import router as store

router = APIRouter()

router.include_router(store, prefix='/bee', tags=['bee'])

