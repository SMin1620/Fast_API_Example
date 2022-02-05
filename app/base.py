from typing import Any, Generic, List, Optional, Type, TypeVar

from sqlmodel import Session, SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class Service(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, session: Session, *, object_in: CreateSchemaType) -> ModelType:
        object_model = self.model.from_orm(object_in)

        session.add(object_model)
        session.commit()

        session.refresh(object_model)
        return object_model

    def find_all(
            self, session: Session, *, offset: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return session.exec(select(self.model).offset(offset).limit(limit)).all()

    def find_one(self, session: Session, id: Any) -> Optional[ModelType]:
        return session.get(self.model, id)

    def update(
            self,
            session: Session,
            *,
            object_model: ModelType,
            object_in: UpdateSchemaType,
    ) -> ModelType:
        update_data = object_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(object_model, key, value)

        session.add(object_model)
        session.commit()

        session.refresh(object_model)
        return object_model

    def remove(self, session: Session, *, object_model: ModelType) -> None:
        session.delete(object_model)
        session.commit()
