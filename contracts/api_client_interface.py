from abc import ABC
from abc import abstractmethod

from typing import Dict
from typing import Any

class ApiClientInterface(ABC):
    @abstractmethod
    def fetch_data(self, url: str) -> Dict[str, Any]:
        pass