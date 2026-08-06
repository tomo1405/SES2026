import pandas as pd
import re
from src_0919 import task_func

def test_task_func():
    data = [[1, 'ABC', 'XYZ'], [2, 'DEF', 'GHI']]
    mapping = {'ABC': '123', 'DEF': '456'}
    expected_output = [[1, '123', 'XYZ'], [2, '456', 'GHI']]
    df = task_func(data, mapping)
    assert df.values.tolist() == expected_output

def test_task_func_with_null_values():
    data = [[1, 'ABC', None], [2, None, 'GHI']]
    mapping = {'ABC': '123', 'DEF': '456'}
    expected_output = [[1, '123', None], [2, None, 'GHI']]
    df = task_func(data, mapping)
    assert df.values.tolist() == expected_output

def test_task_func_with_non_string_values():
    data = [[1, 123, 'XYZ'], [2, 'DEF', 'GHI']]
    mapping = {'ABC': '123', 'DEF': '456'}
    expected_output = [[1, 123, 'XYZ'], [2, 'DEF', 'GHI']]
    df = task_func(data, mapping)
    assert df.values.tolist() == expected_output