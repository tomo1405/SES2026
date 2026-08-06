import pytest
from src_0501 import task_func
import os
import tempfile

def test_task_func_with_valid_data():
    values = [
        {'ID': 1, 'Name': 'Alice', 'Age': 30},
        {'ID': 2, 'Name': 'Bob', 'Age': 25}
    ]
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        result = task_func(values, filename)
        assert os.path.exists(result)
        assert os.path.abspath(filename) == result

    os.remove(filename)

def test_task_func_with_missing_fields():
    values = [
        {'ID': 1, 'Name': 'Alice'},
        {'ID': 2, 'Age': 25}
    ]
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        result = task_func(values, filename)
        assert os.path.exists(result)
        assert os.path.abspath(filename) == result

    os.remove(filename)

def test_task_func_with_empty_data():
    values = []
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
        result = task_func(values, filename)
        assert os.path.exists(result)
        assert os.path.abspath(filename) == result

    os.remove(filename)

def test_task_func_with_invalid_filename():
    values = [{'ID': 1, 'Name': 'Alice', 'Age': 30}]
    with pytest.raises(Exception):
        task_func(values, '/invalid/path/to/file.xls')

def test_task_func_with_nonexistent_directory():
    values = [{'ID': 1, 'Name': 'Alice', 'Age': 30}]
    with pytest.raises(Exception):
        task_func(values, '/nonexistent/directory/file.xls')