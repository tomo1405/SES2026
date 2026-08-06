import collections
import os
import tempfile

import pytest
from src_1000 import task_func


def test_task_func_with_valid_url_and_column():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        temp_file.write(b'name,age\nAlice,30\nBob,25\nCharlie,30')
        temp_file.flush()
        temp_file_path = temp_file.name

    # Mock the URL to point to the temporary file
    url = f'file://{temp_file_path}'
    column_name = 'name'
    result = task_func(url, column_name, 'output.csv')

    assert result == collections.Counter({'Alice': 1, 'Bob': 1, 'Charlie': 1})

    # Clean up
    os.remove(temp_file_path)
    os.remove('output.csv')

def test_task_func_with_invalid_column():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        temp_file.write(b'name,age\nAlice,30\nBob,25\nCharlie,30')
        temp_file.flush()
        temp_file_path = temp_file.name

    # Mock the URL to point to the temporary file
    url = f'file://{temp_file_path}'
    column_name = 'gender'

    with pytest.raises(ValueError) as excinfo:
        task_func(url, column_name, 'output.csv')

    assert str(excinfo.value) == "The provided column_name 'gender' does not exist in the CSV file."

    # Clean up
    os.remove(temp_file_path)

def test_task_func_with_nonexistent_url():
    url = 'http://nonexistenturl.com/file.csv'
    column_name = 'name'

    with pytest.raises(Exception) as excinfo:
        task_func(url, column_name, 'output.csv')

    # No need to clean up as no files are created locally

def test_task_func_with_empty_csv():
    # Create a temporary empty CSV file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        temp_file.write(b'')
        temp_file.flush()
        temp_file_path = temp_file.name

    # Mock the URL to point to the temporary file
    url = f'file://{temp_file_path}'
    column_name = 'name'

    with pytest.raises(ValueError) as excinfo:
        task_func(url, column_name, 'output.csv')

    assert str(excinfo.value) == "The provided column_name 'name' does not exist in the CSV file."

    # Clean up
    os.remove(temp_file_path)