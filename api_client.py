import requests
import urllib3

from typing import Dict
from typing import Any

from logger_config import setup_logger

from contracts import ApiClientInterface

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ApiClient(ApiClientInterface):
    """Клиент для получения данных из метода API"""
    
    def __init__(self, verify_ssl: bool = False):
        """Инициализирует новый экземпляр"""
        self.verify_ssl = verify_ssl
        self.logger = setup_logger(__name__)

    def fetch_data(self, url: str) -> Dict[str, Any]:
        """Получить данные по ссылке"""
        try:
            self.logger.info(f"Попытка взять данные с API: {url}")
            response = requests.get(url, verify=self.verify_ssl)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Не удалось взять данные с API: {e}")
            raise