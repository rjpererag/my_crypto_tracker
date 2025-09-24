import requests


class DataFetcher:

    def __init__(self, host):
        self.host = host

    @staticmethod
    def _get(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def fetch_price_history(self, ticker: str, time_interval) -> list:
        url = f"{self.host}/price-history-minutes/{time_interval}/{ticker}"
        response = self._get(url=url)
        return response.get("data", [])

    def fetch_exchanges(self) -> list:
        url = f"{self.host}/exchanges"
        response = self._get(url=url)
        return response.get("data", [])

    def fetch_symbols(self) -> list:
        url = f"{self.host}/symbols"
        response = self._get(url=url)
        return response.get("data", [])

    def fetch_tickers(self, symbol, exchange) -> list:

        symbol_lower = symbol.lower()
        exchange_lower = exchange.lower()

        url = f"{self.host}/tickers/{symbol_lower}/{exchange_lower}"
        response = self._get(url=url)
        return response.get("data", [])

