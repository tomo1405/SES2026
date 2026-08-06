import re

import pytest
from src_0326 import task_func


def test_task_func_no_files(tmpdir):
    # Create a temporary directory with no files
    dir_path = tmpdir.mkdir("empty_dir")
    
    # Call the function
    result = task_func(str(dir_path))
    
    # Assert that the result is an empty dictionary
    assert result == {}

def test_task_func_single_file_no_matches(tmpdir):
    # Create a temporary directory with a single file containing no matches
    dir_path = tmpdir.mkdir("single_file_no_matches")
    file_path = dir_path.join("test.txt")
    file_path.write("This file has no matches.")
    
    # Call the function
    result = task_func(str(dir_path))
    
    # Assert that the result contains the file with an empty list of matches
    assert result == {"test.txt": []}

def test_task_func_single_file_with_matches(tmpdir):
    # Create a temporary directory with a single file containing matches
    dir_path = tmpdir.mkdir("single_file_with_matches")
    file_path = dir_path.join("test.txt")
    file_path.write("This file has some matches: \\example\\ and \\another\\")
    
    # Call the function
    result = task_func(str(dir_path))
    
    # Assert that the result contains the file with the correct matches
    assert result == {"test.txt": ["\\example\\", "\\another\\"]}

def test_task_func_multiple_files(tmpdir):
    # Create a temporary directory with multiple files
    dir_path = tmpdir.mkdir("multiple_files")
    file1_path = dir_path.join("file1.txt")
    file1_path.write("File 1 has \\match1\\")
    file2_path = dir_path.join("file2.txt")
    file2_path.write("File 2 has \\match2\\ and \\match3\\")
    
    # Call the function
    result = task_func(str(dir_path))
    
    # Assert that the result contains both files with their respective matches
    assert result == {
        "file1.txt": ["\\match1\\"],
        "file2.txt": ["\\match2\\", "\\match3\\"]
    }

def test_task_func_nonexistent_directory():
    # Call the function with a non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func("/nonexistent/directory")

def test_task_func_invalid_regex_pattern(tmpdir):
    # Create a temporary directory with a single file
    dir_path = tmpdir.mkdir("invalid_regex")
    file_path = dir_path.join("test.txt")
    file_path.write("This file has some text.")
    
    # Call the function with an invalid regex pattern
    with pytest.raises(re.error):
        task_func(str(dir_path), regex_pattern=r'(')

def test_task_func_large_file(tmpdir):
    # Create a temporary directory with a large file
    dir_path = tmpdir.mkdir("large_file")
    file_path = dir_path.join("large.txt")
    file_path.write("a" * 10000)  # Large file with no matches
    
    # Call the function
    result = task_func(str(dir_path))
    
    # Assert that the result contains the file with an empty list of matches
    assert result == {"large.txt": []}