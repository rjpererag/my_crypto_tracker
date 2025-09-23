from tracker.tracker_wrapper import CryptoTracker, TrackerSettings

def track_from_exchange(exchange_name: str,
                        tickets: list[str],
                        save_cached_data: bool,
                        execute_params: dict,
                        waiting_time: int,
                        msg_broker_params: dict,
                        ):

    my_settings = TrackerSettings(
        exchange=exchange_name,
        tickets=tickets,
        save_cached_data=save_cached_data,
        execute_params=execute_params,
        waiting_time=waiting_time,
        msg_broker_params=msg_broker_params
    )

    my_tracker = CryptoTracker(tracker_settings=my_settings)
    my_tracker.binance.track()


def main() -> None:
    track_from_exchange(
        exchange_name="binance",
        tickets=["BTCUSDT", "ETHUSDT"],
        save_cached_data=False,
        execute_params={},
        waiting_time=2,
        msg_broker_params={
            "host": "rabbitmq",
            "queue_name": "my_queue",
            "exchange_name": "",
            "routing_key": "my_queue"
        },
    )


if __name__ == "__main__":
    main()

