import duckdb
import pandas as pd

class DuckDBManager:
    def __init__(self, db_name="analytics.db"):
        self.connection = duckdb.connect(db_name)

    def register_dataframe(self, name: str, dataframe: pd.DataFrame):
        self.connection.register(name, dataframe)

    def query(self, sql: str):
        return self.connection.execute(sql).fetchdf()
