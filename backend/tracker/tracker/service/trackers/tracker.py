from typing import Any
from dataclasses import asdict
import datetime
from time import sleep

from ..abstract.tracker_abstract import TrackerAbstract
from ..settings.tracker import TrackerSettings

from ...exchange_api import Exchanges
from ...utils import logger, FileManager
print("Success")

class Tracker(TrackerAbstract):

    def __init__(self,
                 tracker_settings: TrackerSettings,
                 current_tracker: str,
                 **kwargs):

        self.tracker_settings = tracker_settings
        logger.info(f"BUILDING {self.tracker_settings.exchange.upper()} TRACKER")

        self.now = datetime.datetime.now()
        self.now_str = self.now.strftime("%Y%m%d%H%M%S")

        self.execute_params = tracker_settings.execute_params
        self.current_tracker = current_tracker

        self.exchanges = Exchanges()
        self.file_manager = FileManager()

        self.is_valid_tracker = self._validate_tracker()
        self.directories, self.directories_msg = self._create_directories()
        self.cached_data = self._create_cached_data()

        self._save_metadata()

    def _save_metadata(self) -> None:

        path_ = self.directories.get('metadata')
        object_ = self.cached_data.get('metadata')

        self.file_manager.save_json(
            path=f"{path_}/metadata_{self.now_str}.json",
            object_=object_
        )


    def _save_cached_data(self) -> None:

        if self.tracker_settings.save_cached_data:
            data_path = self.directories.get('data', '')
            self.file_manager.save_json(
                path=f"{data_path}/data_{self.now_str}.json",
                object_=self.cached_data["data"]["data"]
            )


    def _create_cached_data(self) -> dict:
        return {
            "data": {"id": [], "data": {}},
            "errors": {},
            "metadata": {
                "timestamp": self.now_str,
                "tracker_settings": asdict(self.tracker_settings),
                "directories": self.directories_msg
            }
        }

    def _create_directories(self) -> tuple[dict , dict | list[dict]]:

        parent_directory = f"{self.tracker_settings.exchange}_cache"
        directory_tree = [
            parent_directory,
            f"{parent_directory}/data",
            f"{parent_directory}/errors",
            f"{parent_directory}/metadata",
            f"{parent_directory}/data/json",
            f"{parent_directory}/errors/json",
            f"{parent_directory}/metadata/json",
        ]

        directories = {
            "directory_tree": directory_tree,
            "data": directory_tree[4],
            "errors": directory_tree[5],
            "metadata": directory_tree[6],
        }

        msg = self.file_manager.create_directory(dirs=directory_tree, mode="multiple")
        return directories, msg

    def _validate_tracker(self) -> bool:
        return self.tracker_settings.exchange.lower().strip() == self.current_tracker.lower().strip()

    def track(self) -> Any:
        if self.is_valid_tracker:
            logger.info(f"   TRACKING: {self.tracker_settings.tickets}")
            while True:
                is_successful, msg = self._track()

                if not is_successful:
                    logger.error(f"Tracker is broke. Reason: {msg}")
                    break

                sleep(self.tracker_settings.waiting_time)

        logger.error(f"TRACKER SETTINGS DOESN'T MATCH WITH CURRENT TRACKER SETTINGS")

    def _validate_response(self,  *args, **kwargs) -> bool:
        ...

    def _track(self):
        ...

