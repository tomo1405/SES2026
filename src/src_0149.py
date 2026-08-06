import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    le = LabelEncoder()
    df[column_name] = le.fit_transform(df[column_name])
    return df