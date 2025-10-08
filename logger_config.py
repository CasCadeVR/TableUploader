import logging
import sys

def setup_logger(name: str, level: str = "INFO"):
    """Конфигурация логирования"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger