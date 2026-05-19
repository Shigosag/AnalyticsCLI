from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AnalyticsCLI")
EXPORT_DIR = os.getenv("EXPORT_DIR", "exports")
DATA_PATH = os.getenv("DATA_PATH", "data/")
LOG_PATH = os.getenv("LOG_PATH", "logs/")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
