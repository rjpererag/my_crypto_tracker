from tracker.tracker_wrapper import CryptoTracker, TrackerSettings

def track_from_exchange(exchange_name: str,
                        tickets: list[str],
                        save_cached_data: bool,
                        execute_params: dict,
                        waiting_time: int
                        ):

    my_settings = TrackerSettings(
        exchange=exchange_name,
        tickets=tickets,
        save_cached_data=save_cached_data,
        execute_params=execute_params,
        waiting_time=waiting_time,
    )

    my_tracker = CryptoTracker(tracker_settings=my_settings)
    my_tracker.binance.track()


def main() -> None:
    track_from_exchange(
        exchange_name="binance",
        tickets=["BTCUSDT", "ETHUSDT"],
        save_cached_data=True,
        execute_params={},
        waiting_time=2
    )


if __name__ == "__main__":
    main()

