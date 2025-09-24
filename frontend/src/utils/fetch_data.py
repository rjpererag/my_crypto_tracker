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
        """http://localhost:5001/price-history-minutes/120%20minute/BTCUSDT"""

        url = f"{self.host}/price-history-minutes/{time_interval}/{ticker}"
        response = self._get(url=url)
        return response.get("data", [])

