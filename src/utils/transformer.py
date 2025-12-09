import pandas as pd

def add_column(df: pd.DataFrame, name: str, func):
    df[name] = df.apply(func, axis=1)
    return df
