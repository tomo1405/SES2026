import pytest
import xlwt
import os
import pandas as pd
from src_0502 import task_func

def test_task_func_invalid_json_str():
    with pytest.raises(TypeError) as exc_info:
        task_func(json_str=123, filename="output.xls")
    assert "json_str must be a string, bytes, or bytearray" in str(exc_info.value)

def test_task_func_invalid_json_str_type():
    with pytest.raises(TypeError) as exc_info:
        task_func(json_str=[1, 2, 3], filename="output.xls")
    assert "json_str must be a string, bytes, or bytearray" in str(exc_info.value)

def test_task_func_invalid_json_str_value():
    with pytest.raises(ValueError) as exc_info:
        task_func(json_str="invalid json", filename="output.xls")
    assert "Invalid JSON string" in str(exc_info.value)

def test_task_func_valid_input():
    json_str = '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]'
    filename = "output.xls"
    result = task_func(json_str=json_str, filename=filename)
    assert result == os.path.abspath(filename)