import pytest
from src_0598 import task_func
import pandas as pd

@pytest.mark.parametrize("data, letter, expected", [
    (pd.DataFrame({'Name': ['John', 'Jane', 'Jim', 'Jenny']}), 'j', pd.Series([2, 1, 1], index=['John', 'Jane', 'Jim'])),
    (pd.DataFrame({'Name': ['John', 'Jane', 'Jim', 'Jenny']}), 'a', pd.Series([1, 1, 1], index=['John', 'Jane', 'Jim'])),
    (pd.DataFrame({'Name': ['John', 'Jane', 'Jim', 'Jenny']}), 'z', pd.Series([0, 0, 0], index=['John', 'Jane', 'Jim'])),
])
def test_task_func(data, letter, expected):
    result = task_func(data, letter)
    assert result.equals(expected)