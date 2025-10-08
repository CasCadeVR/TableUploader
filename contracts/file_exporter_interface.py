from abc import ABC, abstractmethod
from typing import List, Dict

class FileExporterInterface(ABC):
    @abstractmethod
    def export(self, data: List[Dict], api_url: str) -> str:
        pass