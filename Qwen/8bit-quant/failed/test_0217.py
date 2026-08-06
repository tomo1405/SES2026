import pytest
from src_0217 import task_func
import os
import json
from collections import Counter

# Mocking utilities
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_json_files(tmpdir):
    # Create temporary directory and mock JSON files
    file1 = tmpdir.join("file1.json")
    file1.write(json.dumps({"text": "hello world"}))
    
    file2 = tmpdir.join("file2.json")
    file2.write(json.dumps({"text": "world hello"}))
    
    file3 = tmpdir.join("file3.txt")  # Non-json file to be ignored
    file3.write("not a json file")
    
    return str(tmpdir)

def test_task_func(mock_json_files):
    expected_output = [('hello', 2), ('world', 2)]
    result = task_func(mock_json_files, 2)
    assert result == expected_output

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"text": "test test test"}))
def test_task_func_with_empty_directory(mock_open, mock_listdir):
    mock_listdir.return_value = []
    expected_output = []
    result = task_func("/path/to/empty/dir", 3)
    assert result == expected_output

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"text": "a b c d e"}))
def test_task_func_with_limited_word_count(mock_open, mock_listdir):
    mock_listdir.return_value = ["file.json"]
    expected_output = [('a', 1), ('b', 1)]
    result = task_func("/path/to/dir", 2)
    assert result == expected_output

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"text": ""}))
def test_task_func_with_empty_text_in_json(mock_open, mock_listdir):
    mock_listdir.return_value = ["file.json"]
    expected_output = []
    result = task_func("/path/to/dir", 3)
    assert result == expected_output

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({}))
def test_task_func_with_missing_text_key(mock_open, mock_listdir):
    mock_listdir.return_value = ["file.json"]
    expected_output = []
    result = task_func("/path/to/dir", 3)
    assert result == expected_output