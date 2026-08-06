import pytest
from src_0289 import task_func
import os
import json
from tempfile import TemporaryDirectory
from unittest.mock import patch

def create_temp_json_files(temp_dir, files_data):
    for filename, data in files_data.items():
        with open(os.path.join(temp_dir, filename), 'w') as f:
            json.dump(data, f)

@pytest.fixture
def temp_dir_with_json_files():
    with TemporaryDirectory() as temp_dir:
        files_data = {
            'file1.json': {'key1': 1, 'key2': 2},
            'file2.json': {'key2': 3, 'key3': 4},
            'file3.txt': {'not_a_json': True}
        }
        create_temp_json_files(temp_dir, files_data)
        yield temp_dir

def test_task_func(temp_dir_with_json_files):
    result = task_func(temp_dir_with_json_files)
    expected_result = {'key1': 1, 'key2': 5, 'key3': 4}
    assert result == expected_result

def test_task_func_no_json_files(temp_dir_with_json_files):
    # Remove all JSON files to test the case where no JSON files are present
    for filename in os.listdir(temp_dir_with_json_files):
        if filename.endswith('.json'):
            os.remove(os.path.join(temp_dir_with_json_files, filename))
    
    result = task_func(temp_dir_with_json_files)
    assert result == {}

def test_task_func_empty_directory(temp_dir_with_json_files):
    # Clear the directory to test the case where the directory is empty
    for filename in os.listdir(temp_dir_with_json_files):
        os.remove(os.path.join(temp_dir_with_json_files, filename))
    
    result = task_func(temp_dir_with_json_files)
    assert result == {}

def test_task_func_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/non_existent_directory')

@patch('os.listdir')
def test_task_func_os_error(mock_listdir):
    mock_listdir.side_effect = OSError("Mocked OS error")
    with pytest.raises(OSError):
        task_func('/mocked_directory')