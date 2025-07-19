# airport_parking_toolkit/etl.py
import pandas as pd
import logging

def read_and_validate_csv(file_path: str, required_columns: list[str]) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    return df
