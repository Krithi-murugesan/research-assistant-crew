import logging
from core.config import Settings

def setup_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level=Settings.LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    return logging.getLogger(name)
