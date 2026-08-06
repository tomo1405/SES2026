import pytest
from src_0928 import task_func
import pandas as pd
from io import StringIO

# Mock data for testing
MOCK_DATA = """id,name
1,Alice\nBob
2,Charlie
3,Dave\nEve"""

@pytest.fixture
def mock_file():
    return StringIO(MOCK_DATA)

def test_task_func(mock_file):
    # Define expected output after processing
    expected_output = pd.DataFrame({
        'id': [1, 2, 3],
        'name': [0, 1, 2]
    })
    
    # Call the function with the mock file and column name
    result_df = task_func(mock_file, 'name')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_output)

def test_task_func_no_newline(mock_file):
    # Modify the mock data to not contain any newline characters
    mock_file.seek(0)
    mock_data_no_newline = """id,name
1,Alice Bob
2,Charlie
3,Dave Eve"""
    mock_file = StringIO(mock_data_no_newline)
    
    # Define expected output after processing
    expected_output = pd.DataFrame({
        'id': [1, 2, 3],
        'name': [0, 1, 2]
    })
    
    # Call the function with the mock file and column name
    result_df = task_func(mock_file, 'name')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_output)

def test_task_func_empty_file():
    # Create an empty mock file
    empty_file = StringIO("")
    
    # Define expected output after processing
    expected_output = pd.DataFrame(columns=['id', 'name'])
    
    # Call the function with the empty mock file and column name
    result_df = task_func(empty_file, 'name')
    
    # Check if the result matches the expected output
    assert result_df.equals(expected_output)