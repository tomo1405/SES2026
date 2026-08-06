import pytest
from src_1114 import task_func

def test_task_func_with_valid_csv(tmp_path):
    # Create a temporary CSV file
    csv_content = """EMP001,John Doe,Engineering
EMP002,Jane Smith,HR
EMP001,Jim Brown,Marketing"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)
    
    # Call the function
    result = task_func(str(csv_file))
    
    # Assert the result
    assert result == {'EMP001': 2, 'EMP002': 1}

def test_task_func_with_invalid_csv_path():
    # Call the function with a non-existent file path
    result = task_func("non_existent_file.csv")
    
    # Assert the error message
    assert result == {"error": "The file non_existent_file.csv was not found."}

def test_task_func_with_custom_emp_prefix(tmp_path):
    # Create a temporary CSV file with custom prefix
    csv_content = """XYZ001,John Doe,Engineering
XYZ002,Jane Smith,HR
XYZ001,Jim Brown,Marketing"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)
    
    # Call the function with custom prefix
    result = task_func(str(csv_file), emp_prefix='XYZ')
    
    # Assert the result
    assert result == {'XYZ001': 2, 'XYZ002': 1}

def test_task_func_with_no_matching_prefix(tmp_path):
    # Create a temporary CSV file with no matching prefix
    csv_content = """ABC001,John Doe,Engineering
ABC002,Jane Smith,HR
ABC001,Jim Brown,Marketing"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)
    
    # Call the function
    result = task_func(str(csv_file))
    
    # Assert the result
    assert result == {}

def test_task_func_with_empty_csv(tmp_path):
    # Create an empty temporary CSV file
    csv_file = tmp_path / "empty.csv"
    csv_file.touch()
    
    # Call the function
    result = task_func(str(csv_file))
    
    # Assert the result
    assert result == {}