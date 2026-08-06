import re
import pandas as pd
from src_0798 import task_func
import pytest

@pytest.mark.parametrize("df, expected", [
    (pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}), 0),
    (pd.DataFrame({"A": ["({[]})", "[]{}", "{}()"], "B": ["{}[]()", "[][]", "()()"]}), 12),
    (pd.DataFrame({"A": ["({[]})", "[]{}", "{}()"], "B": ["{}[]()", "[][]", "()()"], "C": ["({[]})", "[]{}", "{}()"]}), 24),
])
def test_task_func(df, expected):
    assert task_func(df) == expected