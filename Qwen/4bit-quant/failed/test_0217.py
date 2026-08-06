import pytest
from src_0217 import task_func
import pandas as pd
import os
import json
from collections import Counter

# Mocking utilities
from unittest.mock import patch, mock_open

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({'text': 'hello world'}))
def test_task_func(mock_open, mock_listdir):
    # Setup
    json_dir_path = '/path/to/jsons'
    word_count = 2
    mock_listdir.return_value = ['file1.json', 'file2.json']
    
    # Expected result
    expected_result = [('hello', 2), ('world', 2)]
    
    # Run the function
    result = task_func(json_dir_path, word_count)
    
    # Assert
    assert result == expected_result

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({'text': 'foo bar foo'}))
def test_task_func_with_different_words(mock_open, mock_listdir):
    # Setup
    json_dir_path = '/path/to/jsons'
    word_count = 3
    mock_listdir.return_value = ['file1.json', 'file2.json']
    
    # Expected result
    expected_result = [('foo', 2), ('bar', 1)]
    
    # Run the function
    result = task_func(json_dir_path, word_count)
    
    # Assert
    assert result == expected_result

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({}))
def test_task_func_with_empty_text(mock_open, mock_listdir):
    # Setup
    json_dir_path = '/path/to/jsons'
    word_count = 1
    mock_listdir.return_value = ['file1.json']
    
    # Expected result
    expected_result = []
    
    # Run the function
    result = task_func(json_dir_path, word_count)
    
    # Assert
    assert result == expected_result

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({'text': 'a b c d e'}))
def test_task_func_with_no_files(mock_open, mock_listdir):
    # Setup
    json_dir_path = '/path/to/jsons'
    word_count = 5
    mock_listdir.return_value = []
    
    # Expected result
    expected_result = []
    
    # Run the function
    result = task_func(json_dir_path, word_count)
    
    # Assert
    assert result == expected_result

@patch('os.listdir')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps({'text': 'word1 word2 word3'}))
def test_task_func_with_non_json_file(mock_open, mock_listdir):
    # Setup
    json_dir_path = '/path/to/jsons'
    word_count = 3
    mock_listdir.return_value = ['file1.json', 'file2.txt']
    
    # Expected result
    expected_result = [('word1', 1), ('word2', 1), ('word3', 1)]
    
    # Run the function
    result = task_func(json_dir_path, word_count)
    
    # Assert
    assert result == expected_result