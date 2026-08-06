import matplotlib
import pandas as pd
import pytest
from src_0122 import task_func


def test_task_func_with_valid_input():
    my_list = [1, 2, 3]
    seed = 42
    sales_df, ax = task_func(my_list, seed)
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_with_invalid_input():
    my_list = "not a list"
    seed = 42
    with pytest.raises(TypeError):
        task_func(my_list, seed)

def test_task_func_with_seed():
    my_list = [1, 2, 3]
    seed = 123
    sales_df_1, _ = task_func(my_list, seed)
    seed = 123
    sales_df_2, _ = task_func(my_list, seed)
    assert sales_df_1.equals(sales_df_2)