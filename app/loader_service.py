import pandas as pd
from app.validators import validate_file

class LoaderService:

    @staticmethod
    def load_data(path: str):
        validate_file(path)
        if path.endswith(".csv"):
            return pd.read_csv(path)
        elif path.endswith(".xlsx"):
            return pd.read_excel(path)
        elif path.endswith(".json"):
            return pd.read_json(path)
        else:
            raise ValueError("Unsupported format")
