import json
from datetime import datetime
from time import sleep

from .tracker import Tracker
from ..settings.tracker import TrackerSettings
from ...utils import logger
from ...exchange_api import Ticket




class BinanceTracker(Tracker):

    def __init__(self,
                 tracker_settings: TrackerSettings):
        super().__init__(tracker_settings=tracker_settings,
                         current_tracker="binance")
        self.binance = self.exchanges.binance

    def _create_message(self, tickets: list[Ticket]) -> str:

        def _validate_and_create_message(ticket: Ticket) -> dict:
            is_valid = isinstance(ticket.price, float | int) and isinstance(ticket.symbol, str)
            return {
                "is_valid": is_valid,
                "ticket": {
                    "exchange_name": self.current_tracker,
                    "ticker": ticket.symbol,
                    "price": ticket.price,
                    "timestamp": datetime.now().strftime("%Y%m%d%H%M%S"),  # TODO: CHANGE TO TICKET'S TIMESTAMP
                }
            }

        messages_to_send = [_validate_and_create_message(ticket=ticket) for ticket in tickets]
        return json.dumps(messages_to_send)

    def _track(self) -> tuple[bool, str]:
        try:
            now_str = datetime.now().strftime("%Y%m%d%H%M%S")
            my_tickets = self.binance.get_ticket(
                tickets=self.tracker_settings.tickets
            )

            self.cached_data["data"]["id"].append(now_str)
            self.cached_data["data"]["data"][now_str] = [
                ticket.model_dump() for ticket in my_tickets]

            is_successful = self._validate_response(tickets=my_tickets)
            msg = "No error found"

            self._save_cached_data()

            messages_to_send = self._create_message(tickets=my_tickets)
            self._send_to_broker(message=messages_to_send)

        except Exception as e:
            is_successful = False
            msg = str(e)
            logger.error(f"Error found: {msg}")

        return is_successful, msg


    def _validate_response(self, tickets: list) -> bool:
        if tickets:
            return True
        return False
