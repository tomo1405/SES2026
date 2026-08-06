import base64
import pandas as pd
from src_0550 import task_func
import pytest

def test_task_func():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
    expected_output = 'WwoHMjpcImFcXHMK'

    output = task_func(df)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_null_values():
    df = pd.DataFrame({'col1': [1, None, 3], 'col2': ['a', 'b', None]})
    expected_output = 'WwoHMjowXFwK'

    output = task_func(df)
    assert output == expected_output, "Output does not match expected output"