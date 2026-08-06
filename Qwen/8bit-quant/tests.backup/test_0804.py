import pytest
from src_0804 import task_func
import pandas as pd
from io import StringIO

def test_task_func_no_numeric_columns():
    data = "name,city\nAlice,New York\nBob,Los Angeles"
    file_like_object = StringIO(data)
    with pytest.raises(ValueError) as excinfo:
        task_func(file_like_object)
    assert "Input must at least have one numeric column." in str(excinfo.value)

def test_task_func_with_numeric_columns():
    data = "name,age,salary\nAlice,25,50000\nBob,30,60000"
    file_like_object = StringIO(data)
    result_df = task_func(file_like_object)
    assert isinstance(result_df, pd.DataFrame)
    assert 'age' in result_df.columns and 'salary' in result_df.columns
    assert result_df['age'].min() == 0 and result_df['age'].max() == 1
    assert result_df['salary'].min() == 0 and result_df['salary'].max() == 1

def test_task_func_single_numeric_column():
    data = "name,age\nAlice,25\nBob,30"
    file_like_object = StringIO(data)
    result_df = task_func(file_like_object)
    assert isinstance(result_df, pd.DataFrame)
    assert 'age' in result_df.columns
    assert result_df['age'].min() == 0 and result_df['age'].max() == 1

def test_task_func_empty_file():
    data = ""
    file_like_object = StringIO(data)
    with pytest.raises(pd.errors.EmptyDataError):
        task_func(file_like_object)