import os
from pathlib import Path

import pandas as pd


def load_data(year: int, month: int) -> pd.DataFrame:
    list_path = ["data", f"yellow_tripdata_{year:04d}-{month:02d}.parquet"]

    if "data" not in os.listdir():
        list_path.insert(0, "..")

    filepath = Path(*list_path)
    try:
        df = pd.read_parquet(filepath)
    except:
        raise ValueError(
            f"Data for year {year:04d} and month {month:02d} not found on the data folder"
        )
    return df
