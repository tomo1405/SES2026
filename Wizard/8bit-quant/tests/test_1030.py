python
import pandas as pd
import numpy as np
import pytest

def task_func(rows=100, columns=3):
    column_names = [chr(97 + i) for i in range(columns)]
    values = list("abcdefghijklmnopqrstuvwxyz")
    data = np.random.choice(values, size=(rows, columns))
    df = pd.DataFrame(data, columns=column_names)
    return df

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 3)
    assert set(df.columns) == set("abc")