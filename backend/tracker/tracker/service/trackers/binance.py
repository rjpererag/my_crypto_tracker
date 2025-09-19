from .tracker import Tracker
from ..settings.tracker import TrackerSettings

from datetime import datetime



class BinanceTracker(Tracker):

    def __init__(self, tracker_settings: TrackerSettings):
        super().__init__(tracker_settings=tracker_settings, current_tracker="binance")
        self.binance = self.exchanges.binance

    def _send_data(self):
        # TODO
        """ THIS METHOD WILL BE USED TO SEND THE DATA TO THE DB"""

        if self.cached_data["data"]["id"]:
            last_id = self.cached_data["data"]["id"][-1]
            print(f"Sending {last_id} to db: {self.cached_data['data']['data'][last_id]}")


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
            self._send_data()

        except Exception as e:
            is_successful = False
            msg = str(e)

        return is_successful, msg


    def _validate_response(self, tickets: list) -> bool:
        if tickets:
            return True
        return False
