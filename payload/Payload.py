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
    def clean_amperes(data: int) -> float:
        return Payload.clean_voltage(data)

    @staticmethod
    def clean_temperature(data: int) -> int:
        return data - 40

    @staticmethod
    def clean_percentage(data: int) -> float:
        return data / 100

