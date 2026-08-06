python
import pandas as pd
import pytest
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    le = LabelEncoder()
    df[column_name] = le.fit_transform(df[column_name])
    return df

def test_task_func():
    df = pd.DataFrame({'col1': ['a', 'b', 'c', 'a', 'b', 'c'], 'col2': [1, 2, 3, 4, 5, 6]})
    result = task_func(df, 'col1')
    assert result['col1'].tolist() == [0, 1, 2, 0, 1, 2]