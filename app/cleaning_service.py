import pandas as pd

class CleaningService:

    @staticmethod
    def remove_duplicates(df):
        return df.drop_duplicates()

    @staticmethod
    def fill_missing_values(df):
        return df.fillna(0)
