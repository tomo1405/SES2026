import pandas as pd
from src_1025 import task_func


def test_task_func():
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    expected_df = pd.DataFrame(data_dict)
    expected_plot = 'some_plot_object'

    df, plot = task_func(data_dict)

    assert df.equals(expected_df)
    assert plot == expected_plot