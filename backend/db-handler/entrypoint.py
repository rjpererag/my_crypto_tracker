from service.dbhandler import DBCredentials
from service.dbhandler.crypto_app_db import CryptoAppDBHandler
from service.message_broker import consume_messages


def db_connection() -> CryptoAppDBHandler:
    creds = DBCredentials(
        db_name="postgres",
        db_user="postgres",
        db_password="mypassword",
        db_port="5432",
    )

    return CryptoAppDBHandler(creds=creds, available_exchanges=["binance"])


def main() -> None:
    handler = db_connection()

    msg_broker_params = {
        "host": "rabbitmq",
        "queue_name": "my_queue",
        "exchange_name": "",
        "routing_key": "my_queue"
    }
    consume_messages(conn_settings=msg_broker_params,
                     db_handler=handler)


if __name__ == "__main__":
    main()
