import pytest
from src_0501 import task_func
import os
import tempfile

def test_task_func():
    # Prepare test data
    values = [
        {'ID': 1, 'Name': 'Alice', 'Age': 30},
        {'ID': 2, 'Name': 'Bob', 'Age': 25}
    ]
    filename = 'test_output.xls'

    # Call the function
    result = task_func(values, filename)

    # Check if the file exists and is not empty
    assert os.path.exists(result), f"File {result} does not exist"
    assert os.path.getsize(result) > 0, f"File {result} is empty"

    # Clean up the created file
    os.remove(result)

def test_task_func_missing_fields():
    # Prepare test data with missing fields
    values = [
        {'ID': 1, 'Name': 'Alice'},
        {'ID': 2, 'Age': 25}
    ]
    filename = 'test_output_missing.xls'

    # Call the function
    result = task_func(values, filename)

    # Check if the file exists and is not empty
    assert os.path.exists(result), f"File {result} does not exist"
    assert os.path.getsize(result) > 0, f"File {result} is empty"

    # Clean up the created file
    os.remove(result)

def test_task_func_empty_data():
    # Prepare test data with empty list
    values = []
    filename = 'test_output_empty.xls'

    # Call the function
    result = task_func(values, filename)

    # Check if the file exists and is not empty
    assert os.path.exists(result), f"File {result} does not exist"
    assert os.path.getsize(result) > 0, f"File {result} is empty"

    # Clean up the created file
    os.remove(result)

def test_task_func_invalid_filename():
    # Prepare test data with invalid filename
    values = [
        {'ID': 1, 'Name': 'Alice', 'Age': 30},
        {'ID': 2, 'Name': 'Bob', 'Age': 25}
    ]
    filename = '/invalid/path/test_output.xls'

    # Call the function and expect an OSError
    with pytest.raises(OSError):
        task_func(values, filename)