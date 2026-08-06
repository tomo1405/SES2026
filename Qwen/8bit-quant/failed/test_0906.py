import pytest
from src_0906 import task_func
import os
import tempfile
import csv

def create_temp_csv_files(temp_dir, filenames):
    for filename in filenames:
        with open(os.path.join(temp_dir, f"{filename}.csv"), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['header1', 'header2'])
            writer.writerow(['data1', 'data2'])

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some CSV files in the temporary directory
        create_temp_csv_files(temp_dir, ['file1', 'file2', 'file3'])
        
        # Call the function with the temporary directory path
        result = task_func(temp_dir)
        
        # Check if the result contains the correct keys and values
        assert 'file1' in result
        assert 'file2' in result
        assert 'file3' in result
        
        assert result['file1'] == [['header1', 'header2'], ['data1', 'data2']]
        assert result['file2'] == [['header1', 'header2'], ['data1', 'data2']]
        assert result['file3'] == [['header1', 'header2'], ['data1', 'data2']]

def test_task_func_no_files():
    # Create a temporary directory without any files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Call the function with the empty temporary directory path
        result = task_func(temp_dir)
        
        # Check if the result is an empty dictionary
        assert result == {}

def test_task_func_nonexistent_directory():
    # Use a non-existent directory path
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/directory')

def test_task_func_with_different_extension():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some CSV files in the temporary directory
        create_temp_csv_files(temp_dir, ['file1', 'file2', 'file3'])
        
        # Call the function with a different file extension
        result = task_func(temp_dir, file_extension='.txt')
        
        # Check if the result is an empty dictionary since no .txt files exist
        assert result == {}