import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    if df.select_dtypes(include='number').empty:
        raise ValueError("Input must at least have one numeric column.")

    scaler = MinMaxScaler()
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df