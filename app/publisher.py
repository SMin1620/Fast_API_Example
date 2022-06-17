# rabbitmq_publisher.py
import pika
from pika import BlockingConnection, BasicProperties


def message(topic, message):
    connection = BlockingConnection(
        pika.ConnectionParameters('34.64.142.109')
    )
    try:
        channel = connection.channel()
        props = BasicProperties(content_type='text/plain', delivery_mode=1)
        channel.basic_publish('incoming', topic, message, props)  # incoming exchange로 publish
    finally:
        connection.close()


message('hello.1', 'hello task1')
message('world.2', 'world task2')
