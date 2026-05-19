import pandas as pd

class ProfilingService:

    @staticmethod
    def generate_profile(df: pd.DataFrame):
        profile = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": df.isnull().sum().to_dict(),
            "duplicates": int(df.duplicated().sum()),
            "data_types": df.dtypes.astype(str).to_dict(),
            "summary": df.describe(include="all").to_dict()
        }
        return profile
