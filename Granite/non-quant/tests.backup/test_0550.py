import base64
import pandas as pd
from src_0550 import task_func
import pytest

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_output = 'SFRyaW5nOiAxOjQ6Mzpcbitcclxu'

    actual_output = task_func(df)

    assert actual_output == expected_output