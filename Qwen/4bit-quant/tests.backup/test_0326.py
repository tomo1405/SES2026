import pytest
from src_0326 import task_func
import os
from pathlib import Path

def test_task_func_no_files(tmpdir):
    # Create a temporary directory with no files
    temp_dir = tmpdir.mkdir("test_dir")
    
    result = task_func(str(temp_dir))
    assert result == {}

def test_task_func_single_file_no_matches(tmpdir):
    # Create a temporary directory with one file that does not contain any matches
    temp_dir = tmpdir.mkdir("test_dir")
    temp_file = temp_dir.join("test_file.txt")
    temp_file.write("This is a test file without any matches.")
    
    result = task_func(str(temp_dir))
    assert result == {'test_file.txt': []}

def test_task_func_single_file_with_matches(tmpdir):
    # Create a temporary directory with one file that contains matches
    temp_dir = tmpdir.mkdir("test_dir")
    temp_file = temp_dir.join("test_file.txt")
    temp_file.write("This is a test file with some \\matches\\ and more text.")
    
    result = task_func(str(temp_dir))
    assert result == {'test_file.txt': ['matches']}

def test_task_func_multiple_files(tmpdir):
    # Create a temporary directory with multiple files, some with matches and some without
    temp_dir = tmpdir.mkdir("test_dir")
    temp_file1 = temp_dir.join("test_file1.txt")
    temp_file1.write("This is the first file with \\matches\\.")
    temp_file2 = temp_dir.join("test_file2.txt")
    temp_file2.write("This is the second file without any matches.")
    temp_file3 = temp_dir.join("test_file3.txt")
    temp_file3.write("This is the third file with another \\match\\.")
    
    result = task_func(str(temp_dir))
    assert result == {
        'test_file1.txt': ['matches'],
        'test_file2.txt': [],
        'test_file3.txt': ['match']
    }

def test_task_func_custom_regex(tmpdir):
    # Create a temporary directory with one file using a custom regex pattern
    temp_dir = tmpdir.mkdir("test_dir")
    temp_file = temp_dir.join("test_file.txt")
    temp_file.write("This is a test file with some \\matches\\ and more text.")
    
    result = task_func(str(temp_dir), regex_pattern=r'\w+')
    assert result == {'test_file.txt': ['This', 'is', 'a', 'test', 'file', 'with', 'some', 'and', 'more', 'text']}

def test_task_func_non_existent_directory():
    # Test with a non-existent directory path
    with pytest.raises(FileNotFoundError):
        task_func("/non/existent/directory")

def test_task_func_invalid_regex():
    # Test with an invalid regex pattern
    temp_dir = tmpdir.mkdir("test_dir")
    temp_file = temp_dir.join("test_file.txt")
    temp_file.write("This is a test file with some \\matches\\.")
    
    with pytest.raises(re.error):
        task_func(str(temp_dir), regex_pattern='(')