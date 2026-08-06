import pytest
from src_0830 import task_func

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [10, 20, 30]})
    result_dict = task_func(df)
    assert result_dict == {'Alice': [('Alice', 10)], 'Bob': [('Bob', 20)], 'Charlie': [('Charlie', 30)]}

def test_task_func_invalid_columns():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df[['Name', 'Score']])