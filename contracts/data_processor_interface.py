from abc import ABC
from abc import abstractmethod

from typing import List
from typing import Dict
from typing import Any

class DataProcessorInterface(ABC):
    @abstractmethod
    def process(self, data: Any) -> List[Dict[str, Any]]:
        pass