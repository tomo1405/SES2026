python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pytest

def task_func(data):
    le = LabelEncoder()
    encoded = le.fit_transform(data)
    df = pd.DataFrame({'Category': data, 'Encoded': encoded})

    return df

def test_task_func():
    data = ['A', 'B', 'C', 'A', 'B', 'C']
    expected_df = pd.DataFrame({'Category': ['A', 'B', 'C', 'A', 'B', 'C'], 'Encoded': [0, 1, 2, 0, 1, 2]})
    actual_df = task_func(data)
    assert actual_df.equals(expected_df)