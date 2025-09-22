from dataclasses import dataclass


@dataclass
class TrackerSettings:
    exchange: str | None = None
    tickets: list[str] | None = None
    execute_params: dict | None = None
    save_cached_data: bool = False
    waiting_time: int | None = 10
    msg_broker_params: dict | None = None