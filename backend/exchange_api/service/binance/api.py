from ..requestor import Requestor
from .dataclasses import Ticket
from urllib.parse import quote
import json


class BinanceAPI(Requestor):

    def __init__(self, host: str) -> None:
        self.host = f"https://{host}"

    @staticmethod
    def _encode_tickets(tickets: list[str]) -> str:

        symbols_json = json.dumps(tickets, separators=(',', ':'))
        encoded_symbols = quote(symbols_json)
        return encoded_symbols

    def get_ticket(self, tickets: list[str]) -> list[Ticket]:
        """
        Collect prices from multiple Binance Tickets. Example: ["BTCUSDT", "ETHUSDT"]
        :param tickets:
        :return: list[Ticket]
        """

        base_url = f"{self.host}/api/v3/ticker"
        tickets_encoded = self._encode_tickets(tickets)
        url = f"{base_url}/price?symbols={tickets_encoded}"
        tickets = self._get(url=url)

        return [Ticket(**ticket) for ticket in tickets]
