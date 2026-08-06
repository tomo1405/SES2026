import pytest
from src_0502 import task_func
import os
import pandas as pd

def test_task_func_valid_json():
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30]}'
    filename = "test_output.xls"
    result = task_func(json_str, filename)
    assert os.path.exists(result)
    df = pd.read_excel(result)
    assert df.equals(pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]}))
    os.remove(result)

def test_task_func_invalid_json():
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30}'
    filename = "test_output.xls"
    with pytest.raises(ValueError) as excinfo:
        task_func(json_str, filename)
    assert "Invalid JSON string" in str(excinfo.value)

def test_task_func_non_string_input():
    json_str = 12345
    filename = "test_output.xls"
    with pytest.raises(TypeError) as excinfo:
        task_func(json_str, filename)
    assert "json_str must be a string, bytes, or bytearray" in str(excinfo.value)

def test_task_func_empty_dataframe():
    json_str = '[]'
    filename = "test_output.xls"
    result = task_func(json_str, filename)
    assert os.path.exists(result)
    df = pd.read_excel(result)
    assert df.empty
    os.remove(result)

def test_task_func_existing_file():
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30]}'
    filename = "test_output.xls"
    open(filename, 'a').close()  # Create an empty file
    result = task_func(json_str, filename)
    assert os.path.exists(result)
    df = pd.read_excel(result)
    assert df.equals(pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]}))
    os.remove(result)