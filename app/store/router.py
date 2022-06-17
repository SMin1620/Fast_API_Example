import datetime

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Any
from sqlmodel import Session, select
import logging
import logstash

from app.logger import formatter
from database.session import get_session
from app.store.exceptions import StoreNotFoundException
from app.store.service import service
from app.store.models import Article
from app.my_log import back_logger_info

router = APIRouter()


# logger
log_format = logging.Formatter('\n[%(levelname)s|%(name)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

def create_logger(logger_name):
    logger = logging.getLogger(logger_name)

    # logger already exists
    if len(logger.handlers) > 0:
        return logger

    logger.setLevel(logging.INFO)
    logger.addHandler(logstash.TCPLogstashHandler('34.64.142.109', 5044, version=1))

    filehandler = logging.FileHandler('/Users/iseungmin/PycharmProjects/Fast_API_Example/logs/logfile_{:%Y%m%d}.log'.format(datetime.datetime.now()), encoding='utf-8')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.error('python-logstash: test logstash error message.')
    logger.info('python-logstash: test logstash info message.')
    logger.warning('python-logstash: test logstash warning message.')

    return logger


# test
@router.get("", response_model=List[Article], status_code=status.HTTP_200_OK)
def read_stores(session: Session = Depends(get_session)):

    logger = create_logger('elk-logger')
    logger.info('hello elk-logstash')
    print(logger)

    return service.find_all(session)


# ANCHOR: board document 조회
@router.get("/{article_id}", response_model=Article, status_code=status.HTTP_200_OK)
def read_board(
    *,
    session: Session = Depends(get_session),
    article_id: int,
):
    article = service.find_one(session, article_id)
    if not article:
        raise StoreNotFoundException()

    logger = create_logger('elk-test-logger')
    logger.info('hello elk-test-logstash')
    print(logger)

    return article


# test log 출력
@router.get("/")
def elk_test_show():

    logger = create_logger('elk-test-logger')
    logger.info('hello elk-test-logstash 4')
    print(logger)

    print(logger)

    return "hello world!"


@router.get('log/')
def elk_router():
    back_logger_info("hello world elk")
    return "elk"





