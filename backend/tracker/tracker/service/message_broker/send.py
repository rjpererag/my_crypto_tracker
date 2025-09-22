from ...utils import logger

import pika


def send_message(conn_settings: dict,
                 message):
    """
    RabbitMQ producer. Settings structure:

    conn_settings = {
        'host': <str>,
        'queue_name': <str>,
        'exchange': <str>,
        'routing_key': <str>
        }

    :param conn_settings:
    :param message:
    :return:
    """

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=conn_settings.get('host')))
    channel = connection.channel()

    channel.queue_declare(queue=conn_settings.get('queue_name'))
    channel.basic_publish(exchange=conn_settings.get('exchange_name'),
                          routing_key=conn_settings.get('routing_key'),
                          body=message)

    connection.close()