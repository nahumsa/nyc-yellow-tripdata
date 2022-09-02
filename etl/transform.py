import pandas as pd


def filter_outlier(df: pd.DataFrame, col: str, n_std: int = 3) -> pd.DataFrame:
    _df = df.copy()
    mean = df[col].mean()
    std = df[col].std()
    _df = _df[_df[col] <= mean + n_std * std]
    return _df


def calculate_duration(df: pd.DataFrame) -> pd.DataFrame:
    _df = df.copy()
    _df["duration"] = (
        _df["tpep_dropoff_datetime"] - _df["tpep_pickup_datetime"]
    ).dt.total_seconds()
    return _df


def filter_non_zero_duration(df: pd.DataFrame) -> pd.DataFrame:
    _df = df.copy()
    _df = _df[_df["duration"] > 0.0]
    return _df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    COLUMNS = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "PULocationID",
        "DOLocationID",
    ]

    _df = df.copy()
    _df = _df[COLUMNS]
    _df = calculate_duration(_df)
    _df = filter_non_zero_duration(_df)
    _df = filter_outlier(_df, col="duration")
    # _df = filter_outlier(_df, col="trip_distance", n_std=2)

    return _df
