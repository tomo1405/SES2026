import pytest
from src_0906 import task_func
import os
import tempfile
import csv

def create_temp_file(directory, filename, content):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(content)
    return file_path

def test_task_func_with_csv_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_file(temp_dir, 'file1.csv', [['header1', 'header2'], ['row1col1', 'row1col2']])
        create_temp_file(temp_dir, 'file2.csv', [['headerA', 'headerB'], ['row2col1', 'row2col2']])
        
        result = task_func(temp_dir)
        
        assert len(result) == 2
        assert 'file1' in result
        assert 'file2' in result
        assert result['file1'] == [['header1', 'header2'], ['row1col1', 'row1col2']]
        assert result['file2'] == [['headerA', 'headerB'], ['row2col1', 'row2col2']]

def test_task_func_with_no_csv_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_with_non_csv_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_file(temp_dir, 'file1.txt', [['not', 'a', 'csv']])
        result = task_func(temp_dir)
        assert result == {}

def test_task_func_with_different_extension():
    with tempfile.TemporaryDirectory() as temp_dir:
        create_temp_file(temp_dir, 'file1.json', [['not', 'a', 'csv']])
        create_temp_file(temp_dir, 'file2.csv', [['headerA', 'headerB'], ['row2col1', 'row2col2']])
        
        result = task_func(temp_dir, file_extension='.json')
        
        assert len(result) == 0
        
        result = task_func(temp_dir, file_extension='.csv')
        
        assert len(result) == 1
        assert 'file2' in result
        assert result['file2'] == [['headerA', 'headerB'], ['row2col1', 'row2col2']]

def test_task_func_with_invalid_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/directory')

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == {}