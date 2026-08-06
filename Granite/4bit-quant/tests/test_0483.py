import pandas as pd
import random
import re
import pytest

from src_0483 import task_func

def test_task_func():
    data_list = ["a, b, c", "d, e, f", "g, h, i"]
    seed = 123
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ["Original String", "Modified String"]
    assert df["Original String"].tolist() == ["a, b, c", "d, e, f", "g, h, i"]
    assert df["Modified String"].tolist() == ["b, a, c", "e, d, f", "h, g, i"]

def test_task_func_with_seed():
    data_list = ["a, b, c", "d, e, f", "g, h, i"]
    seed = 123
    df1 = task_func(data_list, seed)
    df2 = task_func(data_list, seed)
    assert df1.equals(df2)

def test_task_func_with_different_seed():
    data_list = ["a, b, c", "d, e, f", "g, h, i"]
    seed1 = 123
    seed2 = 456
    df1 = task_func(data_list, seed1)
    df2 = task_func(data_list, seed2)
    assert not df1.equals(df2)

def test_task_func_with_empty_data_list():
    data_list = []
    seed = 123
    df = task_func(data_list, seed)
    assert df.empty

def test_task_func_with_invalid_seed():
    data_list = ["a, b, c", "d, e, f", "g, h, i"]
    seed = "invalid"
    with pytest.raises(TypeError):
        task_func(data_list, seed)