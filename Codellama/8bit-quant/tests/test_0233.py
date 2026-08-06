import pytest
from src_0233 import task_func
import pandas as pd
import collections

def test_task_func_input_not_df():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_input_df():
    df = pd.DataFrame({'Customer': ['A', 'B', 'C'], 'Sales': [10, 20, 30], 'Category': ['A', 'B', 'C']})
    result = task_func(df)
    assert result['Total Sales'] == 60
    assert result['Most Popular Category'] == 'A'