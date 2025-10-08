import requests
import urllib3
from typing import Dict, Any
from contracts import ApiClientInterface
from logger_config import setup_logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ApiClient(ApiClientInterface):
    def __init__(self, verify_ssl: bool = False):
        self.verify_ssl = verify_ssl
        self.logger = setup_logger(__name__)

    def fetch_data(self, url: str) -> Dict[str, Any]:
        try:
            self.logger.info(f"Fetching data from {url}")
            response = requests.get(url, verify=self.verify_ssl)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch data: {e}")
            raise