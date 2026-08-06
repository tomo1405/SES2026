import pandas as pd
from src_0480 import task_func


def test_task_func_with_empty_list():
    data_list = []
    result_df = task_func(data_list)
    assert result_df.empty
    assert list(result_df.columns) == ["Original String", "Modified String"]

def test_task_func_with_single_empty_string():
    data_list = ["   "]
    result_df = task_func(data_list)
    assert result_df.equals(pd.DataFrame({"Original String": ["   "], "Modified String": ["   "]}))

def test_task_func_with_single_string_no_comma():
    data_list = ["hello"]
    result_df = task_func(data_list)
    assert result_df.equals(pd.DataFrame({"Original String": ["hello"], "Modified String": ["hello"]}))

def test_task_func_with_single_string_with_comma():
    data_list = ["hello, world"]
    result_df = task_func(data_list)
    assert result_df.equals(pd.DataFrame({"Original String": ["hello, world"], "Modified String": ["hello, world"]}))

def test_task_func_with_multiple_strings():
    data_list = ["apple, banana", "cherry, date", "elderberry"]
    result_df = task_func(data_list)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana", "cherry, date", "elderberry"],
        "Modified String": [
            "apple, banana",
            "cherry, date",
            "elderberry"
        ]
    })
    assert result_df.equals(expected_df)

def test_task_func_with_random_replacement():
    data_list = ["apple, banana", "cherry, date", "elderberry"]
    result_df = task_func(data_list, seed=42)
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana", "cherry, date", "elderberry"],
        "Modified String": [
            "apple, banana",
            "cherry, date",
            "elderberry"
        ]
    })
    assert result_df.equals(expected_df)

def test_task_func_with_different_seed():
    data_list = ["apple, banana", "cherry, date", "elderberry"]
    result_df_1 = task_func(data_list, seed=1)
    result_df_2 = task_func(data_list, seed=2)
    assert not result_df_1.equals(result_df_2)