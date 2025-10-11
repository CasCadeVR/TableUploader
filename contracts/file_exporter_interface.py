from abc import ABC
from abc import abstractmethod

from typing import List
from typing import Dict

class FileExporterInterface(ABC):
    @abstractmethod
    def export(self, data: List[Dict], api_url: str) -> str:
        pass