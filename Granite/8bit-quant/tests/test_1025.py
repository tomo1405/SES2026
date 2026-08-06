import pandas as pd
from src_1025 import task_func


def test_task_func():
    data_dict = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]}
    expected_df = pd.DataFrame(data_dict)
    expected_plot = 'Mock plot object'

    df, plot = task_func(data_dict)

    assert df.equals(expected_df)
    assert plot == expected_plot