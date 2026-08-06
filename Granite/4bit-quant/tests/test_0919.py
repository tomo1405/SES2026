import pandas as pd
import re
from src_0919 import task_func

def test_task_func():
    data = [[1, 'ABC', 3], [4, 'DEF', 6], [7, 'GHI', 9]]
    mapping = {'ABC': '123', 'DEF': '456', 'GHI': '789'}
    expected_output = [[1, '123', 3], [4, '456', 6], [7, '789', 9]]

    df = task_func(data, mapping)
    assert df.values.tolist() == expected_output

def test_task_func_with_nan():
    data = [[1, 'ABC', 3], [4, 'DEF', float('nan')], [7, 'GHI', 9]]
    mapping = {'ABC': '123', 'DEF': '456', 'GHI': '789'}
    expected_output = [[1, '123', 3], [4, '456', float('nan')], [7, '789', 9]]

    df = task_func(data, mapping)
    assert df.values.tolist() == expected_output

def test_task_func_with_missing_value():
    data = [[1, 'ABC', 3], [4, None, 6], [7, 'GHI', 9]]
    mapping = {'ABC': '123', 'DEF': '456', 'GHI': '789'}
    expected_output = [[1, '123', 3], [4, None, 6], [7, '789', 9]]

    df = task_func(data, mapping)
    assert df.values.tolist() == expected_output