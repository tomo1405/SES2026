import pytest
from src_0797 import task_func

def test_task_func_no_files(tmpdir):
    # Create an empty directory
    empty_dir = tmpdir.mkdir("empty")
    
    # Call the function with the empty directory
    result = task_func(str(empty_dir))
    
    # Assert that the result is an empty list
    assert result == []

def test_task_func_no_bracket_files(tmpdir):
    # Create a directory with files that do not contain brackets
    no_bracket_dir = tmpdir.mkdir("no_brackets")
    no_bracket_dir.join("file1.txt").write("")
    no_bracket_dir.join("file2.doc").write("")
    
    # Call the function with the directory
    result = task_func(str(no_bracket_dir))
    
    # Assert that the result is an empty list
    assert result == []

def test_task_func_with_bracket_files(tmpdir):
    # Create a directory with files that contain brackets
    bracket_dir = tmpdir.mkdir("brackets")
    bracket_dir.join("file(1).txt").write("")
    bracket_dir.join("file{2}.doc").write("")
    bracket_dir.join("file[3].pdf").write("")
    
    # Call the function with the directory
    result = task_func(str(bracket_dir))
    
    # Assert that the result contains the correct file paths
    expected_files = [
        str(bracket_dir.join("file(1).txt")),
        str(bracket_dir.join("file{2}.doc")),
        str(bracket_dir.join("file[3].pdf"))
    ]
    assert sorted(result) == sorted(expected_files)

def test_task_func_nested_directories(tmpdir):
    # Create a nested directory structure with files containing brackets
    nested_dir = tmpdir.mkdir("nested")
    nested_subdir = nested_dir.mkdir("subdir")
    nested_dir.join("file(1).txt").write("")
    nested_subdir.join("file{2}.doc").write("")
    
    # Call the function with the top-level directory
    result = task_func(str(nested_dir))
    
    # Assert that the result contains the correct file paths
    expected_files = [
        str(nested_dir.join("file(1).txt")),
        str(nested_subdir.join("file{2}.doc"))
    ]
    assert sorted(result) == sorted(expected_files)