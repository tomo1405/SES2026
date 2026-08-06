import pytest
from src_0672 import task_func
import os
import json

def test_task_func_directory_creation(tmp_path):
    directory = tmp_path / "test_dir"
    result = task_func(str(directory), 3)
    assert os.path.exists(result)

def test_task_func_file_creation(tmp_path):
    directory = tmp_path / "test_dir"
    n = 5
    task_func(str(directory), n)
    files = os.listdir(directory)
    assert len(files) == n

def test_task_func_file_content(tmp_path):
    directory = tmp_path / "test_dir"
    n = 3
    task_func(str(directory), n)
    for i in range(n):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = json.load(file)
            assert isinstance(content, dict)
            assert 'number' in content
            assert isinstance(content['number'], int)
            assert 1 <= content['number'] <= 100

def test_task_func_no_files_created(tmp_path):
    directory = tmp_path / "test_dir"
    n = 0
    task_func(str(directory), n)
    files = os.listdir(directory)
    assert len(files) == 0

def test_task_func_existing_directory(tmp_path):
    directory = tmp_path / "test_dir"
    os.makedirs(directory)
    n = 2
    task_func(str(directory), n)
    files = os.listdir(directory)
    assert len(files) == n