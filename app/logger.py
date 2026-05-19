from loguru import logger
import sys
from app.config import LOG_PATH, LOG_LEVEL
import os

os.makedirs(LOG_PATH, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level=LOG_LEVEL, format="{time} | {level} | {message}")
logger.add(f"{LOG_PATH}/app.log", rotation="10 MB", retention="7 days", level="DEBUG")
