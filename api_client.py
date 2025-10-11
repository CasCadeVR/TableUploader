import urllib3
import aiohttp

from typing import Dict
from typing import Any

from contracts import ApiClientInterface

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ApiClient(ApiClientInterface):
    """Клиент для получения данных из метода API"""
    
    def __init__(self, logger, verify_ssl: bool = False):
        """Инициализирует новый экземпляр"""
        self.verify_ssl = verify_ssl
        self.logger = logger

    async def fetch_data(self, url: str) -> Dict[str, Any]:
        """Получить данные по ссылке"""
        try:
            self.logger.info(f"Попытка получить данные по {url}")
            async with aiohttp.ClientSession() as session:
                async with session.get(url, ssl=self.verify_ssl) as response:
                    response.raise_for_status()
                    return await response.json()
                
        except aiohttp.ClientError as e:
            self.logger.error(f"Не удалось получить данные: {e}")
            raise