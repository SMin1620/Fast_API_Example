from fastapi import APIRouter

from app.store.router import router as store
from app.menu.router import router as menu
from app.poll.router import router as poll
from app.poll.router import router as poll

router = APIRouter()

router.include_router(store, prefix='/store', tags=['stores'])
router.include_router(menu, prefix='/menu', tags=['menus'])
router.include_router(poll, prefix='/poll', tags=['polls'])
