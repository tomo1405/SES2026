import pandas as pd
import pytest
from src_0888 import task_func


def test_task_func_default_parameters():
    result = task_func([[1, 2], [3]])
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (50, 6)  # 50 rows and 1 + 2 + 3 = 6 columns

def test_task_func_custom_row_num():
    result = task_func([[1, 2], [3]], row_num=10)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (10, 6)  # 10 rows and 1 + 2 + 3 = 6 columns

def test_task_func_custom_seed():
    df1 = task_func([[1, 2], [3]], seed=42)
    df2 = task_func([[1, 2], [3]], seed=42)
    assert df1.equals(df2)

def test_task_func_empty_input():
    result = task_func([])
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (50, 0)  # 50 rows and 0 columns

def test_task_func_single_element():
    result = task_func([[5]])
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (50, 5)  # 50 rows and 5 columns

def test_task_func_negative_numbers():
    with pytest.raises(ValueError):
        task_func([[-1, 2], [3]])

def test_task_func_non_integer_elements():
    with pytest.raises(ValueError):
        task_func([['a', 2], [3]])