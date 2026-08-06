import matplotlib
import numpy as np
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
    seed = 42
    np.random.seed(seed)
    sales_df, ax = task_func(my_list, seed)
    assert sales_df['Sales'].iloc[0] == 300

def test_task_func_without_seed():
    my_list = [1, 2, 3]
    seed = None
    sales_df, ax = task_func(my_list, seed)
    assert sales_df['Sales'].iloc[0] != 300