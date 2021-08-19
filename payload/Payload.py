from __future__ import annotations

from abc import abstractmethod
from typing import Dict


class Payload:
    @staticmethod
    @abstractmethod
    def parse(data: bytes) -> Dict:
        pass

    # @staticmethod
    # @abstractmethod
    # def __from_struct(data: Dict) -> Payload:
    #     pass
