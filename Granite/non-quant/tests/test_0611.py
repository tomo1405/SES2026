import pytest
from src_0611 import task_func
import pandas as pd

@pytest.fixture
def df():
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [16, 17, 18, 19, 20],
        'E': [21, 22, 23, 24, 25]
    })

@pytest.mark.parametrize("tuples, n_plots, expected_df_shape, expected_num_plots", [
    ([(1, 2), (3, 4)], 2, (3, 5), 2),
    ([(5, 6), (7, 8)], 3, (1, 5), 0),
    ([(9, 10), (11, 12)], 1, (0, 5), 0)
])
def test_task_func(df, tuples, n_plots, expected_df_shape, expected_num_plots):
    result_df, plots = task_func(df, tuples, n_plots)
    assert result_df.shape == expected_df_shape
    assert len(plots) == expected_num_plots