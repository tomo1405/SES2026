import pytest
from src_0502 import task_func
import pandas as pd
import xlwt
import os

def test_task_func_valid_json_str():
    json_str = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'
    filename = 'test.xls'
    result = task_func(json_str, filename)
    assert result == os.path.abspath(filename)
    assert os.path.exists(filename)
    data = pd.read_excel(filename)
    assert data.shape == (2, 2)
    assert list(data.columns) == ['name', 'age']
    assert data.iloc[0, 0] == 'John'
    assert data.iloc[0, 1] == 30
    assert data.iloc[1, 0] == 'Jane'
    assert data.iloc[1, 1] == 25
    os.remove(filename)

def test_task_func_invalid_json_str():
    json_str = '{"name": "John", "age": 30}'
    filename = 'test.xls'
    with pytest.raises(ValueError) as e:
        task_func(json_str, filename)
    assert 'Invalid JSON string' in str(e.value)

def test_task_func_non_str_json_str():
    json_str = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
    filename = 'test.xls'
    with pytest.raises(TypeError) as e:
        task_func(json_str, filename)
    assert 'json_str must be a string, bytes, or bytearray' in str(e.value)

def test_task_func_invalid_filename():
    json_str = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]'
    filename = 'test.xlsx'
    with pytest.raises(Exception) as e:
        task_func(json_str, filename)
    assert 'Error in file writing' in str(e.value)