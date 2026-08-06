import pytest
from src_0720 import task_func

def test_task_func_empty_directory(tmpdir):
    # Create an empty directory
    empty_dir = tmpdir.mkdir("empty_dir")
    
    # Call the function with the empty directory and a word
    result = task_func(str(empty_dir), "test")
    
    # Assert that the count is 0 since there are no files
    assert result == 0

def test_task_func_single_file_no_match(tmpdir):
    # Create a directory and add a file with no matches
    dir_with_files = tmpdir.mkdir("dir_with_files")
    test_file = dir_with_files.join("testfile.txt")
    test_file.write("This is a test file without the word.")
    
    # Call the function with the directory and a word that doesn't match
    result = task_func(str(dir_with_files), "example")
    
    # Assert that the count is 0 since there are no matches
    assert result == 0

def test_task_func_single_file_match(tmpdir):
    # Create a directory and add a file with a match
    dir_with_files = tmpdir.mkdir("dir_with_files")
    test_file = dir_with_files.join("testfile.txt")
    test_file.write("This is a test file with the word example.")
    
    # Call the function with the directory and a word that matches
    result = task_func(str(dir_with_files), "example")
    
    # Assert that the count is 1 since there is one match
    assert result == 1

def test_task_func_multiple_files(tmpdir):
    # Create a directory and add multiple files with different matches
    dir_with_files = tmpdir.mkdir("dir_with_files")
    file1 = dir_with_files.join("file1.txt")
    file1.write("This is a test file with the word example.")
    file2 = dir_with_files.join("file2.txt")
    file2.write("This is another test file with the word example.")
    file3 = dir_with_files.join("file3.txt")
    file3.write("This file does not have the word example.")
    
    # Call the function with the directory and a word that matches in two files
    result = task_func(str(dir_with_files), "example")
    
    # Assert that the count is 2 since there are two matches
    assert result == 2

def test_task_func_case_insensitive(tmpdir):
    # Create a directory and add a file with a match in different cases
    dir_with_files = tmpdir.mkdir("dir_with_files")
    test_file = dir_with_files.join("testfile.txt")
    test_file.write("This is a test file with the word Example.")
    
    # Call the function with the directory and a word that matches regardless of case
    result = task_func(str(dir_with_files), "example")
    
    # Assert that the count is 1 since there is one match
    assert result == 1

def test_task_func_punctuation(tmpdir):
    # Create a directory and add a file with a match surrounded by punctuation
    dir_with_files = tmpdir.mkdir("dir_with_files")
    test_file = dir_with_files.join("testfile.txt")
    test_file.write("This is a test file with the word 'example'.")
    
    # Call the function with the directory and a word that matches despite punctuation
    result = task_func(str(dir_with_files), "example")
    
    # Assert that the count is 1 since there is one match
    assert result == 1