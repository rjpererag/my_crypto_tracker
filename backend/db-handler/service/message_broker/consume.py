import pika
import json
from ..utils import logger


def decode_message(body: bytes) -> list[dict] | None:
    try:
        message_str = body.decode('utf-8')
        return json.loads(message_str)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        logger.error(f"Error decoding message: {e}")
        return None

def consume_messages(conn_settings: dict, db_handler):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=conn_settings.get('host')))

    channel = connection.channel()
    channel.queue_declare(queue=conn_settings.get('queue_name'))

    # Here que must create the DB Handler function
    def callback(ch, method, properties, body):
        message_decoded = decode_message(body=body)
        for msg in message_decoded:
            if msg.get("is_valid"):
                try:
                    db_handler.insert_price(price_data=msg.get("ticket"))
                    logger.info("Message inserted: {}".format(message_decoded))
                except Exception as e:
                    logger.info(f"Message NOT inserted: {message_decoded}. {str(e)}")


    channel.basic_consume(queue=conn_settings.get('queue_name'),
                          on_message_callback=callback,
                          auto_ack=True)

    logger.info("Waiting for messages")
    channel.start_consuming()
