from app.base import Service

from .models import Store, StoreCreate, StoreUpdate


class StoreService(Service[Store, StoreCreate, StoreUpdate]):
    pass


service = StoreService(Store)
