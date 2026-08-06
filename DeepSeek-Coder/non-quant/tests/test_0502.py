import pytest
from src_0502 import task_func
import os
import pandas as pd
import xlwt

# Test cases for task_func

def test_task_func_valid_input():
    json_str = '{"key": "value"}'
    filename = "test.xls"
    result = task_func(json_str=json_str, filename=filename)
    assert os.path.exists(result)
    os.remove(result)

def test_task_func_invalid_input():
    json_str = b'invalid_json'
    filename = "test.xls"
    with pytest.raises(ValueError):
        task_func(json_str=json_str, filename=filename)

def test_task_func_empty_data():
    json_str = "{}"
    filename = "test.xls"
    result = task_func(json_str=json_str, filename=filename)
    assert os.path.exists(result)
    os.remove(result)