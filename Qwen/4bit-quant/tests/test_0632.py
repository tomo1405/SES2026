import pytest
from src_0632 import task_func
import pandas as pd
import os

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    filename = 'test_output.csv'
    output_dir = './test_output'
    
    # Ensure the test output directory does not exist before running the test
    if os.path.exists(output_dir):
        os.rmdir(output_dir)
    
    result = task_func(sample_df, filename, output_dir)
    
    # Check if the directory was created
    assert os.path.exists(output_dir)
    
    # Check if the file was created
    expected_file_path = os.path.join(output_dir, filename)
    assert os.path.isfile(expected_file_path)
    
    # Check if the returned path is absolute
    assert os.path.isabs(result)
    
    # Clean up after the test
    os.remove(expected_file_path)
    os.rmdir(output_dir)

def test_task_func_default_output_dir(sample_df):
    filename = 'default_output.csv'
    
    # Ensure the default output directory does not exist before running the test
    if os.path.exists(task_func.OUTPUT_DIR):
        os.rmdir(task_func.OUTPUT_DIR)
    
    result = task_func(sample_df, filename)
    
    # Check if the default directory was created
    assert os.path.exists(task_func.OUTPUT_DIR)
    
    # Check if the file was created
    expected_file_path = os.path.join(task_func.OUTPUT_DIR, filename)
    assert os.path.isfile(expected_file_path)
    
    # Check if the returned path is absolute
    assert os.path.isabs(result)
    
    # Clean up after the test
    os.remove(expected_file_path)
    os.rmdir(task_func.OUTPUT_DIR)