python
import numpy as np
import pandas as pd
import pytest

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length, min_value=0, max_value=100):
    """
    Generate a DataFrame with random data and calculate the cumulative distribution function (CDF) for each column.

    Args:
        length (int): The number of rows in the DataFrame.
        min_value (int, optional): The minimum value for each column. Defaults to 0.
        max_value (int, optional): The maximum value for each column. Defaults to 100.

    Returns:
        pd.DataFrame: A DataFrame with random data and the cumulative distribution function (CDF) for each column.
    """

    # Generate random data and create a DataFrame
    data = np.random.randint(min_value, max_value, size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate the cumulative distribution function (CDF) for each column
    df = df.apply(lambda x: x.value_counts().sort_index().cumsum())

    return df

# Test the function
def test_task_func():
    # Test with default arguments
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.iloc[0, 0] == 0
    assert df.iloc[9, 4] == 100

    # Test with custom arguments
    df = task_func(5, min_value=1, max_value=10)
    assert df.shape == (5, 5)
    assert df.iloc[0, 0] == 1
    assert df.iloc[4, 4] == 10

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(10, min_value=100, max_value=1)