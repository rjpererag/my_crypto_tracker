from abc import ABC, abstractmethod


class RequestorAbstract(ABC):

    @abstractmethod
    def _get(self, *args, **kwargs):
        """To handle GET method from the request library"""

        ...

    @abstractmethod
    def _post(self, *args, **kwargs):
        """To handle POST method from the request library"""
        ...