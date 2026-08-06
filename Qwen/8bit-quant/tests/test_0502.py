import os

import pandas as pd
import pytest
import xlwt
from src_0502 import task_func


def test_task_func_valid_json_string(tmpdir):
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30]}'
    filename = str(tmpdir.join("test_output.xls"))
    result = task_func(json_str, filename)
    assert os.path.exists(result)
    df = pd.read_excel(filename)
    assert df.equals(pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]}))

def test_task_func_empty_json_string(tmpdir):
    json_str = '{}'
    filename = str(tmpdir.join("empty_output.xls"))
    result = task_func(json_str, filename)
    assert os.path.exists(result)
    df = pd.read_excel(filename)
    assert df.empty

def test_task_func_invalid_json_string():
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30]'
    with pytest.raises(ValueError) as excinfo:
        task_func(json_str, "invalid_output.xls")
    assert "Invalid JSON string" in str(excinfo.value)

def test_task_func_non_string_input():
    json_str = 12345
    with pytest.raises(TypeError) as excinfo:
        task_func(json_str, "non_string_input.xls")
    assert "json_str must be a string, bytes, or bytearray" in str(excinfo.value)

def test_task_func_file_write_error(monkeypatch):
    def mock_save(self, filename):
        raise IOError("Mocked I/O error")
    monkeypatch.setattr(xlwt.Workbook, 'save', mock_save)
    with pytest.raises(Exception) as excinfo:
        task_func('{"name": ["Alice", "Bob"], "age": [25, 30]}', "file_write_error.xls")
    assert "Error in file writing" in str(excinfo.value)