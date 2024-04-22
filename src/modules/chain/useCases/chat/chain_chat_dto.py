from typing import List

from src.core.base_class import BaseClass


class HistoryDTO(BaseClass):
    role: str
    content: str


class ChainChatDTO(BaseClass):
    input: str
    system: str
    history: List[HistoryDTO]
