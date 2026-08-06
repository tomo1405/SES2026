python
import pytest
from src_0502 import task_func

def test_task_func():
    # Test case 1: Valid JSON string, valid filename, valid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    filename = "test.xls"
    sheet_name = "sheet1"
    result = task_func(json_str, filename, sheet_name)
    assert result == os.path.abspath(filename)
    
    # Test case 2: Valid JSON string, valid filename, invalid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    filename = "test.xls"
    sheet_name = "invalid sheet name"
    with pytest.raises(ValueError):
        task_func(json_str, filename, sheet_name)
    
    # Test case 3: Invalid JSON string, valid filename, valid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"'
    filename = "test.xls"
    sheet_name = "sheet1"
    with pytest.raises(ValueError):
        task_func(json_str, filename, sheet_name)
    
    # Test case 4: Valid JSON string, invalid filename, valid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    filename = "test.txt"
    sheet_name = "sheet1"
    with pytest.raises(Exception):
        task_func(json_str, filename, sheet_name)