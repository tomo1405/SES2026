import re
import random
import pandas as pd
import pytest

from src_0481 import task_func

def test_task_func():
    data_list = ["apple, banana, carrot", "dog, cat, mouse", "a, b, c, d, e"]
    seed = 42
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ["Original String", "Shuffled String"]
    assert df["Original String"].tolist() == data_list
    for s in df["Shuffled String"]:
        substrings = re.split("\s*,\s*", s)
        assert len(substrings) == len(data_list[0].split(", "))
        assert set(substrings) == set(data_list[0].split(", "))

def test_task_func_seed():
    data_list = ["apple, banana, carrot", "dog, cat, mouse", "a, b, c, d, e"]
    seed = 42
    df1 = task_func(data_list, seed)
    df2 = task_func(data_list, seed)
    assert df1.equals(df2)

def test_task_func_no_seed():
    data_list = ["apple, banana, carrot", "dog, cat, mouse", "a, b, c, d, e"]
    df1 = task_func(data_list)
    df2 = task_func(data_list)
    assert not df1.equals(df2)