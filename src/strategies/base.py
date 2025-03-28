from abc import ABC, abstractmethod

from helpers import Response
from src.data_readers import DataReader


class BaseStrategy(ABC):
    data: DataReader

    @abstractmethod
    def calculate_result(self) -> Response: ...

    def __init__(self, data: DataReader) -> None:
        self.data = data
