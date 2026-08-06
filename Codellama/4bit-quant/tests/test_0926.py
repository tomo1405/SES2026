import numpy as np
import pandas as pd
from src_0926 import task_func


def test_task_func():
    # Test that the function returns a pandas DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the function returns a DataFrame with the correct number of rows and columns
    assert task_func().shape == (1000, 5)

    # Test that the function correctly replaces values less than 10 with -1
    assert np.all(task_func()[task_func() < 10] == -1)

    # Test that the function returns a DataFrame with the correct column names
    assert np.all(task_func().columns == ['A', 'B', 'C', 'D', 'E'])

    # Test that the function returns a DataFrame with the correct data types
    assert np.all(task_func().dtypes == np.int64)