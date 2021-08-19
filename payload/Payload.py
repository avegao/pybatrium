from __future__ import annotations

from abc import abstractmethod
from typing import Dict


class Payload:
    @staticmethod
    @abstractmethod
    def parse(data: bytes) -> Dict:
        pass

    @staticmethod
    def clean_voltage(data: int) -> float:
        return data / 1000

    @staticmethod
    def clean_temperature(data: int) -> int:
        return data - 40
