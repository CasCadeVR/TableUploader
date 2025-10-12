from typing import Any
from typing import Dict
from typing import List

from contracts import DataProcessorInterface

from logger_config import setup_logger

def process_value(value: Any, column_name: str = "") -> str:
    """Обработать значение"""
    
    if value is None:
        return ""
    
    elif isinstance(value, dict):
        type_name = column_name if column_name else "Object"
        return f"{type_name}"
    
    elif isinstance(value, list):
        element_type = column_name if column_name else "Object"
        return f"List<{element_type}>:{len(value)}"
    
    else:
        return str(value)


class DataProcessor(DataProcessorInterface):
    def __init__(self):
        """Инициализирует новый экземпляр"""
        self.logger = setup_logger(__name__)


    def process(self, data) -> List[Dict[str, str]]:
        """Обработать данные из словаря"""
        _possible_dict_outcomes = ('data', 'results')
        
        if isinstance(data, list):
            return self._process_list(data)
        
        elif isinstance(data, dict):
            for key in _possible_dict_outcomes:
                if key in data and isinstance(data[key], list):
                    return self._process_list(data[key])
                
            return [data]
        
        else:
            self.logger.warning("Неподдерживаемый тип данных для обработки")
            return []
        
        
    def _process_list(self, data: List) -> List[Dict[str, str]]:
        processed = []
        
        for item in data:
            if isinstance(item, dict):
                processed.append({k: process_value(v, k) for k, v in item.items()})
                
            else:
                self.logger.warning(f"Найден элемент не типа словаря при его обраотке: {item}")
                
        return processed