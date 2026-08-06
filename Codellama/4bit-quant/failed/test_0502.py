import pytest
from src_0502 import task_func

def test_task_func_valid_json_str():
    json_str = '{"name": "John Doe", "age": 30}'
    filename = "test_file.xls"
    sheet_name = "sheet1"
    expected_output = os.path.abspath(filename)
    actual_output = task_func(json_str, filename, sheet_name)
    assert actual_output == expected_output

def test_task_func_invalid_json_str():
    json_str = "invalid json string"
    filename = "test_file.xls"
    sheet_name = "sheet1"
    with pytest.raises(ValueError):
        task_func(json_str, filename, sheet_name)

def test_task_func_empty_json_str():
    json_str = ""
    filename = "test_file.xls"
    sheet_name = "sheet1"
    with pytest.raises(ValueError):
        task_func(json_str, filename, sheet_name)

def test_task_func_invalid_filename():
    json_str = '{"name": "John Doe", "age": 30}'
    filename = "test_file.xls"
    sheet_name = "sheet1"
    with pytest.raises(ValueError):
        task_func(json_str, filename, sheet_name)

def test_task_func_invalid_sheet_name():
    json_str = '{"name": "John Doe", "age": 30}'
    filename = "test_file.xls"
    sheet_name = ""
    with pytest.raises(ValueError):
        task_func(json_str, filename, sheet_name)