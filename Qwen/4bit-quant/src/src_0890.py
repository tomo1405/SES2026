import os
import pandas as pd
import numpy as np
def task_func(data_dir: str, csv_file: str) -> pd.DataFrame:
    file_path = os.path.join(data_dir, csv_file)
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.number):  # checking for numeric columns
            df[column].fillna(df[column].mean(), inplace=True)

    return df