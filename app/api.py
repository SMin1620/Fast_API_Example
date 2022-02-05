from fastapi import APIRouter

from app.store.router import router as store
from app.menu.router import router as menu

router = APIRouter()

router.include_router(store, prefix='/store', tags=['stores'])
router.include_router(menu, prefix='/menu', tags=['menus'])
