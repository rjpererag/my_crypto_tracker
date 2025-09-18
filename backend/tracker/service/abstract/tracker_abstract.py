from abc import ABC, abstractmethod
from typing import Any


class TrackerAbstract(ABC):

    @abstractmethod
    def _validate_tracker(self) -> Any:
        ...

    @abstractmethod
    def _validate_response(self, *args, **kwargs) -> Any:
        ...

    @abstractmethod
    def _track(self) -> Any:
        ...

    @abstractmethod
    def track(self) -> Any:
        ...