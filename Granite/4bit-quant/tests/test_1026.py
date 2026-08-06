import pytest
from src_1026 import task_func

def test_task_func():
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df_scaled, ax = task_func(data_dict)

    assert df_scaled.shape == (3, 3)
    assert ax.get_title() == "Scaled Values"

def test_task_func_with_empty_data():
    data_dict = {'A': [1, 2, 3], 'B': [None, None, None], 'C': [7, 8, 9]}
    df_scaled, ax = task_func(data_dict)

    assert df_scaled.empty
    assert ax.get_title() == "Scaled Values"