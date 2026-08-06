import pytest
from src_0502 import task_func

def test_task_func_with_valid_json():
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30]}'
    filename = "test_output.xls"
    result = task_func(json_str, filename)
    assert os.path.exists(result)
    os.remove(result)

def test_task_func_with_invalid_json():
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30}'
    filename = "test_output.xls"
    with pytest.raises(ValueError) as excinfo:
        task_func(json_str, filename)
    assert "Invalid JSON string" in str(excinfo.value)

def test_task_func_with_non_string_input():
    json_str = 12345
    filename = "test_output.xls"
    with pytest.raises(TypeError) as excinfo:
        task_func(json_str, filename)
    assert "json_str must be a string, bytes, or bytearray" in str(excinfo.value)

def test_task_func_with_empty_json():
    json_str = '[]'
    filename = "test_output.xls"
    result = task_func(json_str, filename)
    assert os.path.exists(result)
    os.remove(result)

def test_task_func_with_custom_sheet_name():
    json_str = '{"name": ["Alice", "Bob"], "age": [25, 30]}'
    filename = "test_output.xls"
    sheet_name = "CustomSheet"
    result = task_func(json_str, filename, sheet_name=sheet_name)
    assert os.path.exists(result)
    os.remove(result)