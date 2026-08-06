python
import pandas as pd
import pytest
from src_0149 import task_func

def test_task_func():
    df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1, 2, 3]})
    result = task_func(df, 'col1')
    expected = pd.DataFrame({'col1': [0, 1, 2], 'col2': [1, 2, 3]})
    assert result.equals(expected)