python
import numpy as np
import pandas as pd
import pytest

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length, min_value=0, max_value=100):
    # Generate random data and create a DataFrame
    data = np.random.randint(min_value, max_value, size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate the cumulative distribution function (CDF) for each column
    df = df.apply(lambda x: x.value_counts().sort_index().cumsum())

    return df

def test_task_func():
    # Test case 1: length = 10, min_value = 0, max_value = 100
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.iloc[0, 0] == 0
    assert df.iloc[9, 0] == 90
    assert df.iloc[0, 1] == 1
    assert df.iloc[9, 1] == 10
    assert df.iloc[0, 2] == 1
    assert df.iloc[9, 2] == 10
    assert df.iloc[0, 3] == 1
    assert df.iloc[9, 3] == 10
    assert df.iloc[0, 4] == 1
    assert df.iloc[9, 4] == 10

    # Test case 2: length = 100, min_value = 10, max_value = 200
    df = task_func(100, 10, 200)
    assert df.shape == (100, 5)
    assert df.iloc[0, 0] == 10
    assert df.iloc[99, 0] == 1900
    assert df.iloc[0, 1] == 1
    assert df.iloc[99, 1] == 10
    assert df.iloc[0, 2] == 1
    assert df.iloc[99, 2] == 10
    assert df.iloc[0, 3] == 1
    assert df.iloc[99, 3] == 10
    assert df.iloc[0, 4] == 1
    assert df.iloc[99, 4] == 10