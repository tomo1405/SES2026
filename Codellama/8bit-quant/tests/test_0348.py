import pytest
from src_0348 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    df = pd.DataFrame({'column': ['abcdefghijklmnopqrstuvwxyz', '1234567890', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']})
    result = task_func(df, 'column')
    expected = pd.Series({'abcdefghijklmnopqrstuvwxyz': 1, '1234567890': 1, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 1})
    pd.testing.assert_series_equal(result, expected)