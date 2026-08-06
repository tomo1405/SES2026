import pytest
from src_0479 import task_func

def test_task_func_no_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, fox", "grape, honeydew"]
    df = task_func(data_list)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Original String", "Modified String"]
    assert len(df) == len(data_list)

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "dog, elephant, fox", "grape, honeydew"]
    seed = 42
    df1 = task_func(data_list, seed=seed)
    df2 = task_func(data_list, seed=seed)
    assert df1.equals(df2)

def test_task_func_single_element():
    data_list = ["single"]
    df = task_func(data_list)
    assert len(df) == 1
    assert df.loc[0, "Original String"] == "single"
    assert df.loc[0, "Modified String"] == "single"

def test_task_func_empty_list():
    data_list = []
    df = task_func(data_list)
    assert df.empty

def test_task_func_special_characters():
    data_list = ["!@#, $%^&*()", "123, 456, 789"]
    df = task_func(data_list)
    assert len(df) == len(data_list)
    for original, modified in zip(df["Original String"], df["Modified String"]):
        assert original != modified

def test_task_func_whitespace_handling():
    data_list = ["   apple,   banana,   cherry   "]
    df = task_func(data_list)
    assert df.loc[0, "Original String"] == "apple, banana, cherry"
    assert df.loc[0, "Modified String"] != "apple, banana, cherry"

def test_task_func_repeated_substrings():
    data_list = ["apple, apple, apple"]
    df = task_func(data_list)
    assert df.loc[0, "Modified String"] != "apple, apple, apple"