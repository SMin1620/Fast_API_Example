from typing import Generator

from sqlmodel import Session
from .db import engine


def get_session() -> Generator:
    with Session(engine) as session:
        yield session

