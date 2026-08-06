import pytest
from src_0874 import task_func
import os
import tempfile

def test_task_func_valid_data():
    data = [
        [1, 2],
        [3, 4]
    ]
    headers = ['A', 'B']
    file_path = tempfile.NamedTemporaryFile(delete=False).name

    try:
        result = task_func(data, file_path, headers)
        assert os.path.exists(result)
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            assert rows == [['A', 'B'], ['1', '2'], ['3', '4']]
    finally:
        os.remove(file_path)

def test_task_func_missing_headers():
    data = [
        [1, 2],
        [3, 4]
    ]
    headers = ['A']
    file_path = tempfile.NamedTemporaryFile(delete=False).name

    try:
        result = task_func(data, file_path, headers)
        assert os.path.exists(result)
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            assert rows == [['A'], ['1', 'None'], ['3', 'None']]
    finally:
        os.remove(file_path)

def test_task_func_invalid_file_path():
    data = [
        [1, 2],
        [3, 4]
    ]
    headers = ['A', 'B']
    file_path = None

    with pytest.raises(ValueError, match="The file path is invalid."):
        task_func(data, file_path, headers)

def test_task_func_empty_data():
    data = []
    headers = ['A', 'B']
    file_path = tempfile.NamedTemporaryFile(delete=False).name

    try:
        result = task_func(data, file_path, headers)
        assert os.path.exists(result)
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            assert rows == [['A', 'B']]
    finally:
        os.remove(file_path)

def test_task_func_no_data_rows():
    data = [
        [],
        []
    ]
    headers = ['A', 'B']
    file_path = tempfile.NamedTemporaryFile(delete=False).name

    try:
        result = task_func(data, file_path, headers)
        assert os.path.exists(result)
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            assert rows == [['A', 'B'], ['None', 'None'], ['None', 'None']]
    finally:
        os.remove(file_path)