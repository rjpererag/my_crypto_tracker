from .binance import BinanceAPI


class Exchanges:

    def __init__(self):

        self.binance = BinanceAPI(
            host="api.binance.com"
        )