import pytest
from src_0848 import task_func
import os
import random
import string

@pytest.fixture
def setup_directory(tmpdir):
    # Create a temporary directory for testing
    temp_dir = tmpdir.mkdir("temp_text_files")
    return str(temp_dir)

def test_task_func(setup_directory):
    input_string = "Hello, world!\nThis is a test."
    expected_file_count = 2
    file_paths = task_func(input_string, directory=setup_directory)
    
    # Check if the correct number of files were created
    assert len(file_paths) == expected_file_count
    
    # Check if each file exists and contains the correct content
    for file_path in file_paths:
        assert os.path.exists(file_path)
        with open(file_path, 'r') as file:
            content = file.read()
            # Remove punctuation from the input string to match the file content
            expected_content = re.sub('['+string.punctuation+']', '', input_string.split('\n')[file_paths.index(file_path)])
            assert content == expected_content

def test_task_func_empty_input(setup_directory):
    input_string = ""
    expected_file_count = 0
    file_paths = task_func(input_string, directory=setup_directory)
    
    # Check if no files were created
    assert len(file_paths) == expected_file_count

def test_task_func_single_line(setup_directory):
    input_string = "Single line"
    expected_file_count = 1
    file_paths = task_func(input_string, directory=setup_directory)
    
    # Check if one file was created
    assert len(file_paths) == expected_file_count
    
    # Check if the file exists and contains the correct content
    for file_path in file_paths:
        assert os.path.exists(file_path)
        with open(file_path, 'r') as file:
            content = file.read()
            # Remove punctuation from the input string to match the file content
            expected_content = re.sub('['+string.punctuation+']', '', input_string)
            assert content == expected_content