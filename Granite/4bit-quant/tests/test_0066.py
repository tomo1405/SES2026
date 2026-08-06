import pandas as pd
import matplotlib.pyplot as plt
from src_0066 import task_func
import pytest

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['col1', 'col2', 'col3'])
    expected_ax = None  # You would need to mock the matplotlib functions for this

    df, ax = task_func(data)

    assert df.equals(expected_df)
    assert ax == expected_ax