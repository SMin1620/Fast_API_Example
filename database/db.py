from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# mysql 연동
app = {
    'name': 'mysql+pymysql',
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'dbconn': 'fast_test',
    'port': '3306'
}


SQLALCHEMY_DATABASE_URL = f'{app["name"]}://{app["user"]}:{app["password"]}@{app["host"]}:{app["port"]}/{app["dbconn"]}'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='utf-8'
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()