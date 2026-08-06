import pandas as pd
import seaborn as sns
import pytest
from src_0067 import task_func

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_df = pd.DataFrame([[1, 2, 2], [4, 5, 2], [7, 8, 2]], columns=COLUMNS)
    expected_ax = None  # Replace with the expected output of ax

    df, ax = task_func(data)

    assert df.equals(expected_df)
    assert ax == expected_ax