from abc import ABC, abstractmethod
from typing import Any


class TrackerAbstract(ABC):

    @abstractmethod
    def execute(self) -> Any:
        ...