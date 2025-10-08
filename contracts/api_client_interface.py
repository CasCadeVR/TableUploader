from abc import ABC, abstractmethod
from typing import Dict, Any

class ApiClientInterface(ABC):
    @abstractmethod
    def fetch_data(self, url: str) -> Dict[str, Any]:
        pass