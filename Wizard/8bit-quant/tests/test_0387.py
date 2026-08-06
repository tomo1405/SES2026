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

# Test the function
def test_task_func():
    # Test case 1: Test with default arguments
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.iloc[0, 0] == 0
    assert df.iloc[9, 4] == 100

    # Test case 2: Test with custom arguments
    df = task_func(5, min_value=50, max_value=150)
    assert df.shape == (5, 5)
    assert df.iloc[0, 0] == 50
    assert df.iloc[4, 4] == 150

    # Test case 3: Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(10, min_value=150, max_value=50)