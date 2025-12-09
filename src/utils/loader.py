import pandas as pd
import pyarrow.parquet as pq


def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path, engine="pyarrow")


def load_parquet(path: str) -> pd.DataFrame:
    return pq.read_table(path).to_pandas()
