import pytest
from src_0380 import task_func

def test_task_func_output_type():
    length = 5
    result = task_func(length)
    assert isinstance(result, pd.DataFrame), "The output should be a pandas DataFrame"

def test_task_func_columns():
    length = 5
    result = task_func(length)
    assert list(result.columns) == COLUMNS, "The DataFrame should have the correct columns"

def test_task_func_length():
    length = 5
    result = task_func(length)
    assert len(result) == length, "The number of rows in the DataFrame should match the input length"

def test_task_func_data_range():
    length = 5
    result = task_func(length)
    assert result.values.min() >= 0 and result.values.max() <= 99, "The values in the DataFrame should be within the range 0 to 99"

def test_task_func_empty_dataframe():
    length = 0
    result = task_func(length)
    assert result.empty, "A DataFrame with length 0 should be empty"