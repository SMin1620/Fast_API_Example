from app.base import Service

from .models import Store, StoreRead


class StoreService(Service[Store, StoreRead]):
    pass


service = StoreService(Store)
