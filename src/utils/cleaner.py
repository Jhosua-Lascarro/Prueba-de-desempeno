import pandas as pd

def clean_text_column(df: pd.DataFrame, column: str, regex: str = None) -> pd.DataFrame:
    # Default regex removes symbols like @ / \ { } _ ! # % ( = * )
    default_regex = r"[@/\\{}(!_#%()=*]"
    pattern = regex if regex is not None else default_regex

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(pattern, "", regex=True)
        .str.normalize('NFKD')
        .str.encode('ascii', 'ignore')
        .str.decode('utf-8')
    )
    return df
