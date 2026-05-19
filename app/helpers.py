from pathlib import Path
import pandas as pd
from app.logger import logger

def ensure_directory(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)

def load_csv(path: str):
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded CSV: {path}")
        return df
    except Exception as e:
        logger.error(f"Error loading CSV: {e}")
        raise
