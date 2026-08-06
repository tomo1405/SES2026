import random
import string
import pandas as pd
import pytest

from src_0480 import task_func

def test_task_func():
    data_list = ["apple,banana,cherry", "1,2,3", "", "mango,grape,watermelon"]
    seed = 0
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (4, 2)
    assert df["Original String"].tolist() == data_list
    assert df["Modified String"].tolist() != data_list

def test_task_func_with_seed():
    data_list = ["apple,banana,cherry", "1,2,3", "", "mango,grape,watermelon"]
    seed = 42
    df = task_func(data_list, seed)
    assert df["Modified String"].tolist() != data_list

def test_task_func_with_empty_data():
    data_list = [""] * 10
    seed = 0
    df = task_func(data_list, seed)
    assert df["Modified String"].tolist() == data_list