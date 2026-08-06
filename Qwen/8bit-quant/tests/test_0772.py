import pytest
from src_0772 import task_func
import os
from pathlib import Path
import csv

@pytest.fixture
def setup_test_directory(tmpdir):
    # Create a temporary directory
    temp_dir = tmpdir.mkdir("test_dir")
    # Create some test files
    (temp_dir / "file1-1.csv").write_text("col1,col2\nval1,val2")
    (temp_dir / "file2-2.csv").write_text("col3,col4\nval3,val4")
    (temp_dir / "file3.txt").write_text("This is a text file.")
    return str(temp_dir)

def test_task_func(setup_test_directory):
    directory = setup_test_directory
    pattern = r'^(.*?)-\d+\.csv$'
    
    result = task_func(directory, pattern)
    
    # Check if the correct files were created
    expected_files = ['file1.csv', 'file2.csv']
    assert set(result) == set(expected_files)
    
    # Check if the content of the new files is correct
    for file in expected_files:
        with open(Path(directory) / file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if file == 'file1.csv':
                assert rows == [['col1', 'col2'], ['val1', 'val2']]
            elif file == 'file2.csv':
                assert rows == [['col3', 'col4'], ['val3', 'val4']]

def test_task_func_no_matching_files(tmpdir):
    temp_dir = tmpdir.mkdir("no_match_dir")
    (temp_dir / "file1.txt").write_text("This is a text file.")
    directory = str(temp_dir)
    
    result = task_func(directory)
    
    assert result == []

def test_task_func_empty_directory(tmpdir):
    temp_dir = tmpdir.mkdir("empty_dir")
    directory = str(temp_dir)
    
    result = task_func(directory)
    
    assert result == []