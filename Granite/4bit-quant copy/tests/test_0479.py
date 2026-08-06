import pandas as pd
import re
import random
import pytest

from src_0479 import task_func

def test_task_func():
    data_list = ["apple, banana, orange", "grape, melon, watermelon", "lemon, lime, grapefruit"]
    seed = 42
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert "Original String" in df.columns
    assert "Modified String" in df.columns
    for s in data_list:
        substrings = re.split(", ", s)
        random_substring = random.choice(substrings)
        modified_s = (
            s.replace(", " + random_substring, "")
            if ", " + random_substring in s
            else s.replace(random_substring + ", ", "")
        )
        assert modified_s in df["Modified String"].values

def test_task_func_with_seed():
    data_list = ["apple, banana, orange", "grape, melon, watermelon", "lemon, lime, grapefruit"]
    seed = 42
    df1 = task_func(data_list, seed)
    df2 = task_func(data_list, seed)
    assert df1.equals(df2)

def test_task_func_without_seed():
    data_list = ["apple, banana, orange", "grape, melon, watermelon", "lemon, lime, grapefruit"]
    df1 = task_func(data_list)
    df2 = task_func(data_list)
    assert not df1.equals(df2)