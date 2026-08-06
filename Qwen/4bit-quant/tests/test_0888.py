import pandas as pd
import pytest
from src_0888 import task_func


def test_task_func_default_parameters():
    # Test with default parameters
    df = task_func([[1, 2], [3, 4]])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 10)  # 1 + 2 + 3 + 4 = 10 columns

def test_task_func_custom_row_num():
    # Test with custom row_num
    df = task_func([[1, 2], [3, 4]], row_num=100)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 10)

def test_task_func_custom_seed():
    # Test with custom seed for reproducibility
    df1 = task_func([[1, 2], [3, 4]], seed=42)
    df2 = task_func([[1, 2], [3, 4]], seed=42)
    assert df1.equals(df2)

def test_task_func_single_column():
    # Test with a single column
    df = task_func([[5]])
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50, 5)

def test_task_func_no_columns():
    # Test with no columns
    with pytest.raises(ValueError):
        task_func([[]])

def test_task_func_empty_list():
    # Test with an empty list
    with pytest.raises(ValueError):
        task_func([])