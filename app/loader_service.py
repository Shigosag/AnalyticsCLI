import pandas as pd
import polars as pl
from app.validators import validate_file

class LoaderService:

    @staticmethod
    def load_data(path: str, use_polars: bool = False):
        validate_file(path)
        if path.endswith(".csv"):
            return pl.read_csv(path) if use_polars else pd.read_csv(path)
        elif path.endswith(".xlsx"):
            return pl.read_excel(path) if use_polars else pd.read_excel(path)
        elif path.endswith(".json"):
            return pl.read_json(path) if use_polars else pd.read_json(path)
        else:
            raise ValueError("Unsupported format")
