import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    """Хранение всех настроек приложения"""
    
    API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/users")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")
    VERIFY_SSL = os.getenv("VERIFY_SSL", "False").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")