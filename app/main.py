from fastapi import FastAPI
from database.db import engine
from sqlmodel import SQLModel
from fastapi.responses import RedirectResponse

from app.api import router

app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    SQLModel.metadata.create_all(bind=engine)


@app.get("/", response_class=RedirectResponse)
def root() -> str:
    return "/docs"


# router
app.include_router(router)

