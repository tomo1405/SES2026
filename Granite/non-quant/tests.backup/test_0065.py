import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pytest
from src_0065 import task_func

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_analyzed_df = pd.DataFrame({
        'col1': [1, 4, 7],
        'col2': [2, 5, 8],
        'col3': [3, 6, 9]
    })
    expected_ax = None  # You can replace this with the expected output of the function

    analyzed_df, ax = task_func(data)

    pd.testing.assert_frame_equal(analyzed_df, expected_analyzed_df)
    assert ax == expected_ax