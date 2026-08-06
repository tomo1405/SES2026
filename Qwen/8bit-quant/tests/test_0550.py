import pandas as pd
from src_0550 import task_func


def test_task_func_with_empty_dataframe():
    input_df = pd.DataFrame()
    expected_output = "ZmFtaWx5X25hbWUsY29sdW1uZF9uYW1lCg=="
    assert task_func(input_df) == expected_output

def test_task_func_with_single_row():
    input_df = pd.DataFrame({"column_name": ["value"]})
    expected_output = "ZmFtaWx5X25hbWUsY29sdW1uZF9uYW1lCnZhbHVlCg=="
    assert task_func(input_df) == expected_output

def test_task_func_with_multiple_rows():
    input_df = pd.DataFrame({"column_name": ["value1", "value2"]})
    expected_output = "ZmFtaWx5X25hbWUsY29sdW1uZF9uYW1lCnZhbHVlMQp2YWx1ZTIK"
    assert task_func(input_df) == expected_output

def test_task_func_with_different_column_names():
    input_df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
    expected_output = "bmFtZSxhZ2UKQWxpY2UsMzAKQm9iLDI1Cg=="
    assert task_func(input_df) == expected_output

def test_task_func_with_special_characters():
    input_df = pd.DataFrame({"column_name": ["value@1", "value#2"]})
    expected_output = "ZmFtaWx5X25hbWUsY29sdW1uZF9uYW1lCnZhbHVlQDEKdmFsdWUjMgp="
    assert task_func(input_df) == expected_output