python
import pytest
from src_0502 import task_func

def test_task_func():
    # Test case 1: Valid JSON string, valid filename, valid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    filename = "test.xls"
    sheet_name = "test_sheet"
    expected_result = os.path.abspath(filename)
    result = task_func(json_str, filename, sheet_name)
    assert result == expected_result
    
    # Test case 2: Valid JSON string, valid filename, invalid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    filename = "test.xls"
    sheet_name = "test sheet"
    with pytest.raises(Exception) as e:
        task_func(json_str, filename, sheet_name)
    assert str(e.value) == "Error in file writing: Sheet name must be a string of length <= 31."
    
    # Test case 3: Invalid JSON string, valid filename, valid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"'
    filename = "test.xls"
    sheet_name = "test_sheet"
    with pytest.raises(ValueError) as e:
        task_func(json_str, filename, sheet_name)
    assert str(e.value) == "Invalid JSON string: Extra data: line 1 column 2 - line 1 column 16 (char 17)"
    
    # Test case 4: Valid JSON string, invalid filename, valid sheet name
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    filename = "test"
    sheet_name = "test_sheet"
    with pytest.raises(Exception) as e:
        task_func(json_str, filename, sheet_name)
    assert str(e.value) == "Error in file writing: File name must end with .xls or .xlsx."
    
    # Test case 5: Valid JSON string, valid filename, sheet name with length > 31
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    filename = "test.xls"
    sheet_name = "test_sheet_name_is_a_very_long_name_which_is_longer_than_31_characters"
    with pytest.raises(Exception) as e:
        task_func(json_str, filename, sheet_name)
    assert str(e.value) == "Error in file writing: Sheet name must be a string of length <= 31."