import csv
import os
import tempfile

import pytest
from src_0874 import task_func


def test_task_func_valid_data():
    # Arrange
    data = [
        ['Alice', 30],
        ['Bob', 25]
    ]
    headers = ['Name', 'Age']
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name

    # Act
    result = task_func(data, file_path, headers)

    # Assert
    assert os.path.exists(result)
    with open(result, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert rows == [headers] + data

    # Cleanup
    os.remove(result)

def test_task_func_missing_data():
    # Arrange
    data = [
        ['Alice', 30],
        ['Bob']  # Missing age
    ]
    headers = ['Name', 'Age']
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name

    # Act
    result = task_func(data, file_path, headers)

    # Assert
    assert os.path.exists(result)
    with open(result, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert rows == [headers, ['Alice', 30], ['Bob', None]]

    # Cleanup
    os.remove(result)

def test_task_func_invalid_file_path():
    # Arrange
    data = [
        ['Alice', 30],
        ['Bob', 25]
    ]
    headers = ['Name', 'Age']
    file_path = None

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        task_func(data, file_path, headers)
    assert str(excinfo.value) == "The file path is invalid."

def test_task_func_no_headers():
    # Arrange
    data = [
        ['Alice', 30],
        ['Bob', 25]
    ]
    headers = []
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name

    # Act & Assert
    with pytest.raises(IndexError):
        task_func(data, file_path, headers)

    # Cleanup
    os.remove(result)