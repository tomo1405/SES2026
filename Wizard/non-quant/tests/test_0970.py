python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    if df.select_dtypes(include=np.number).shape[1] != df.shape[1]:
        raise TypeError("Input DataFrame contains non-numeric data types.")
    if df.empty or df.isnull().values.any():
        raise ValueError("Input DataFrame is empty or contains NaN values.")

    df_cumsum = df.cumsum()
    scaler = MinMaxScaler()
    df_norm_cumsum = pd.DataFrame(scaler.fit_transform(df_cumsum), columns=df.columns)

    return df_norm_cumsum

def test_task_func():
    # Test case 1: Valid input DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_output = pd.DataFrame({'A': [1, 3, 6], 'B': [4, 9, 15]})
    assert task_func(df).equals(expected_output)

    # Test case 2: Input DataFrame contains non-numeric data types
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['4', '5', '6']})
    with pytest.raises(TypeError):
        task_func(df)

    # Test case 3: Input DataFrame is empty or contains NaN values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, np.nan]})
    with pytest.raises(ValueError):
        task_func(df)