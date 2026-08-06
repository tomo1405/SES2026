import numpy as np
import pandas as pd
import pytest
from src_0348 import task_func

# Constants
PATTERN = r"([a-fA-F\d]{32})"

# Sample data
df = pd.DataFrame({
    'column': ['abc1234567890abcdef1234567890abcdef', 'def4567890abcdef1234567890abcdefabc', 'ghi7890abcdef1234567890abcdefabc456']
})

# Test cases
def test_task_func():
    counts = task_func(df, 'column')
    assert isinstance(counts, pd.Series)
    assert len(counts) == 3
    assert counts.iloc[0] == 1
    assert counts.iloc[1] == 1
    assert counts.iloc[2] == 1

def test_task_func_empty_column():
    df_empty = pd.DataFrame({
        'column': ['', '  ', np.nan]
    })
    counts = task_func(df_empty, 'column')
    assert isinstance(counts, pd.Series)
    assert len(counts) == 0

def test_task_func_invalid_column():
    with pytest.raises(KeyError):
        task_func(df, 'invalid_column')

def test_task_func_invalid_pattern():
    df_invalid = pd.DataFrame({
        'column': ['abc1234567890abcdef1234567890abcdefg', 'def4567890abcdef1234567890abcdefabcd', 'ghi7890abcdef1234567890abcdefabc4567']
    })
    with pytest.raises(ValueError):
        task_func(df_invalid, 'column')