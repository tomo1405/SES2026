import pytest
from src_0068 import task_func
import pandas as pd
import os
import tempfile
import re

def create_temp_files(temp_dir, files):
    for file_name in files:
        with open(os.path.join(temp_dir, file_name), 'w') as f:
            f.write('Sample content')

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir

def test_task_func_with_default_pattern(temp_dir):
    files = ['EMP1.txt', 'EMP2.txt', 'NO_EMP3.txt']
    create_temp_files(temp_dir, files)
    
    expected_df = pd.DataFrame({
        'File': ['EMP1.txt', 'EMP2.txt'],
        'Size': [len('Sample content')] * 2
    })

    result_df = task_func(temp_dir)
    assert result_df.equals(expected_df)

def test_task_func_with_custom_pattern(temp_dir):
    files = ['ABC1.txt', 'XYZ2.txt', 'ABC3.txt']
    create_temp_files(temp_dir, files)
    
    expected_df = pd.DataFrame({
        'File': ['ABC1.txt', 'ABC3.txt'],
        'Size': [len('Sample content')] * 2
    })

    result_df = task_func(temp_dir, pattern='^ABC')
    assert result_df.equals(expected_df)

def test_task_func_no_matching_files(temp_dir):
    files = ['NO_EMP1.txt', 'NO_EMP2.txt']
    create_temp_files(temp_dir, files)
    
    expected_df = pd.DataFrame(columns=['File', 'Size'])

    result_df = task_func(temp_dir)
    assert result_df.equals(expected_df)

def test_task_func_empty_directory(temp_dir):
    expected_df = pd.DataFrame(columns=['File', 'Size'])

    result_df = task_func(temp_dir)
    assert result_df.equals(expected_df)