from decouple import config

from service.dbhandler import DBCredentials
from service.dbhandler.crypto_app_db import CryptoAppDBHandler
from service.message_broker import consume_messages


def db_connection() -> CryptoAppDBHandler:
    creds = DBCredentials(
        db_host=config("POSTGRES_HOST"),
        db_name=config("POSTGRES_DB"),
        db_user=config("POSTGRES_USER"),
        db_password=config("POSTGRES_PASSWORD"),
        db_port=config("POSTGRES_PORT"),
    )

    return CryptoAppDBHandler(creds=creds, available_exchanges=["binance"])


def main() -> None:
    handler = db_connection()

    msg_broker_params = {
        "host": config("RABBITMQ_HOST"),
        "queue_name": config("RABBITMQ_QUEUE_NAME"),
        "exchange_name": config("RABBITMQ_EXCHANGE_NAME"),
        "routing_key": config("RABBITMQ_ROUTING_KEY")
    }
    consume_messages(conn_settings=msg_broker_params,
                     db_handler=handler)


if __name__ == "__main__":
    main()
