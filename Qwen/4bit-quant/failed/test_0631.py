import pytest
from src_0631 import task_func
import pandas as pd
import os

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, None],
        'B': [None, 4, 5]
    }
    df = pd.DataFrame(data)

    # Define filename and output directory
    filename = 'test_file.json'
    output_dir = './output'

    # Call the function
    result = task_func(df, filename, output_dir)

    # Check if the output directory exists
    assert os.path.exists(output_dir), "Output directory does not exist"

    # Check if the file was created
    expected_file_path = os.path.join(output_dir, filename)
    assert os.path.isfile(expected_file_path), "File was not created"

    # Check if the function returns the correct file path
    assert result == expected_file_path, "Function did not return the correct file path"

    # Read the content of the file to verify its contents
    with open(expected_file_path, 'r') as f:
        content = f.read()

    # Define the expected JSON content
    expected_content = '[{"A": 1, "B": null}, {"A": 2, "B": 4}, {"A": null, "B": 5}]'

    # Check if the file content matches the expected content
    assert content == expected_content, "File content does not match the expected content"

# Clean up after tests
def teardown_module(module):
    if os.path.exists('./output'):
        os.remove(os.path.join('./output', 'test_file.json'))
        os.rmdir('./output')