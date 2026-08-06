python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    if df.select_dtypes(include=np.number).shape[1] != df.shape[1]:
        raise TypeError("Input DataFrame contains non-numeric data types.")
    if df.empty or df.isnull().values.any():
        raise ValueError("Input DataFrame is empty or contains NaN values.")

    df_cumsum = df.cumsum()
    scaler = MinMaxScaler()
    df_norm_cumsum = pd.DataFrame(scaler.fit_transform(df_cumsum), columns=df.columns)

    return df_norm_cumsum

# Test case 1
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df_norm_cumsum = task_func(df)
print(df_norm_cumsum)

# Test case 2
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['4', '5', '6']})
try:
    df_norm_cumsum = task_func(df)
except TypeError as e:
    print(e)

# Test case 3
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, np.nan]})
try:
    df_norm_cumsum = task_func(df)
except ValueError as e:
    print(e)

# Test case 4
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
try:
    df_norm_cumsum = task_func(df)
except ValueError as e:
    print(e)