from abc import ABC, abstractmethod
from typing import List, Dict, Any

class DataProcessorInterface(ABC):
    @abstractmethod
    def process(self, data: Any) -> List[Dict[str, Any]]:
        pass