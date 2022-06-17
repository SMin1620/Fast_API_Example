from app.base import Service

from app.store.models import Article, ArticleCreate, ArticleUpdate

class StoreService(Service[Article, ArticleCreate, ArticleUpdate]):
    pass


service = StoreService(Article)
