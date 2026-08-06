import pytest
from src_0371 import task_func
import os
import json
import tempfile
import shutil

@pytest.fixture
def setup_temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def create_json_files(temp_dir):
    files = [
        {"name": "file1.json", "content": {"key": "value1"}},
        {"name": "file2.json", "content": {"key": "value2"}},
    ]
    for file_info in files:
        file_path = os.path.join(temp_dir, file_info["name"])
        with open(file_path, 'w') as file:
            json.dump(file_info["content"], file)
    return [os.path.join(temp_dir, file["name"]) for file in files]

def test_task_func(setup_temp_dir, create_json_files):
    processed_files = task_func(setup_temp_dir)
    assert len(processed_files) == 2
    for file_path in processed_files:
        assert os.path.exists(file_path)
        with open(file_path, 'r') as file:
            content = json.load(file)
            assert content == {"key": "value1"} or content == {"key": "value2"}

def test_task_func_nonexistent_directory():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("nonexistent_directory")
    assert str(excinfo.value) == "Directory nonexistent_directory not found."

def test_task_func_no_json_files(setup_temp_dir):
    processed_files = task_func(setup_temp_dir)
    assert processed_files == []

def test_task_func_empty_json_file(setup_temp_dir):
    file_path = os.path.join(setup_temp_dir, "empty.json")
    with open(file_path, 'w') as file:
        json.dump({}, file)
    processed_files = task_func(setup_temp_dir)
    assert len(processed_files) == 1
    with open(file_path, 'r') as file:
        content = json.load(file)
        assert content == {}