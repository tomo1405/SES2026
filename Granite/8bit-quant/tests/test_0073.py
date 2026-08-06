import pandas as pd
import os
import numpy as np
import ast
from src_0073 import task_func
def test_task_func_with_csv_file():
    directory = "path/to/directory"
    df_expected = pd.DataFrame({
        'email': ['a@example.com', 'b@example.com', 'c@example.com'],
        'list': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        'sum': [6, 15, 24],
        'mean': [2.0, 5.0, 8.0],
        'median': [2.0, 5.0, 8.0]
    })
    fig_expected = "matplotlib.pyplot.Figure"
    df_actual, fig_actual = task_func(directory)
    pd.testing.assert_frame_equal(df_actual, df_expected)
    assert type(fig_actual) == fig_expected
def test_task_func_with_no_csv_file():
    directory = "path/to/empty/directory"
    df_expected = pd.DataFrame({}, columns = ['email', 'list'] + ['sum', 'mean', 'median'])
    fig_expected = None
    df_actual, fig_actual = task_func(directory)
    pd.testing.assert_frame_equal(df_actual, df_expected)
    assert fig_actual == fig_expected