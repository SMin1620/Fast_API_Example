from app.base import Service

from .models import Store, StoreCreate


class StoreService(Service[Store, StoreCreate]):
    pass


service = StoreService(Store)
