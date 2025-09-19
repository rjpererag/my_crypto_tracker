from .service.settings.tracker import TrackerSettings
from .service.trackers import BinanceTracker


class CryptoTracker:

    def __init__(self, tracker_settings: TrackerSettings):
        self.binance = BinanceTracker(tracker_settings=tracker_settings)
