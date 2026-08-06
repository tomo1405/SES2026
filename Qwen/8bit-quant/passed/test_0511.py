import pytest
from src_0511 import task_func
import gzip
import os

# Helper function to create temporary gzip files
def create_temp_gzip_file(content, temp_file_path):
    with gzip.open(temp_file_path, 'wt') as f:
        f.write(content)

@pytest.fixture
def temp_files(tmpdir):
    file1_path = str(tmpdir.join('file1.gz'))
    file2_path = str(tmpdir.join('file2.gz'))
    
    content1 = "line1\nline2\nline3\n"
    content2 = "line1\nchanged_line2\nline3\n"
    
    create_temp_gzip_file(content1, file1_path)
    create_temp_gzip_file(content2, file2_path)
    
    yield file1_path, file2_path
    
    # Clean up temporary files
    os.remove(file1_path)
    os.remove(file2_path)

def test_task_func(temp_files):
    file1_path, file2_path = temp_files
    result = task_func(file1_path, file2_path)
    expected_output = "- line2\n+ changed_line2\n"
    assert result == expected_output

def test_task_func_identical_files(temp_files):
    file1_path, file2_path = temp_files
    # Make both files identical
    with gzip.open(file2_path, 'wt') as f:
        f.write("line1\nline2\nline3\n")
    
    result = task_func(file1_path, file2_path)
    expected_output = ""
    assert result == expected_output

def test_task_func_empty_files(temp_files):
    file1_path, file2_path = temp_files
    # Make both files empty
    with gzip.open(file1_path, 'wt') as f:
        f.write("")
    with gzip.open(file2_path, 'wt') as f:
        f.write("")
    
    result = task_func(file1_path, file2_path)
    expected_output = ""
    assert result == expected_output

def test_task_func_single_line_files(temp_files):
    file1_path, file2_path = temp_files
    # Make both files have single lines
    with gzip.open(file1_path, 'wt') as f:
        f.write("single_line\n")
    with gzip.open(file2_path, 'wt') as f:
        f.write("different_single_line\n")
    
    result = task_func(file1_path, file2_path)
    expected_output = "- single_line\n+ different_single_line\n"
    assert result == expected_output