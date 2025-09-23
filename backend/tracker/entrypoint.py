from decouple import config
from tracker.tracker_wrapper import CryptoTracker, TrackerSettings

def track_from_binance(
        save_cached_data: bool,
        execute_params: dict,
        waiting_time: int,
        msg_broker_params: dict,
):

    my_settings = TrackerSettings(
        exchange="binance",
        tickets=["BTCUSDT", "ETHUSDT"],
        save_cached_data=save_cached_data,
        execute_params=execute_params,
        waiting_time=waiting_time,
        msg_broker_params=msg_broker_params
    )

    my_tracker = CryptoTracker(tracker_settings=my_settings)
    my_tracker.binance.track()


def main() -> None:
    track_from_binance(
        save_cached_data=config("TRACKER_SAVE_CACHED_DATA", cast=bool, default=False),
        execute_params={},
        waiting_time=config("TRACKER_WAITING_TIME", cast=int, default=10),
        msg_broker_params={
            "host": config("RABBITMQ_HOST"),
            "queue_name": config("RABBITMQ_QUEUE_NAME"),
            "exchange_name": config("RABBITMQ_EXCHANGE_NAME"),
            "routing_key": config("RABBITMQ_ROUTING_KEY")
        },
    )


if __name__ == "__main__":
    main()

