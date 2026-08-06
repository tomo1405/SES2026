import pytest
from src_0631 import task_func
import pandas as pd
import os
import json

def test_task_func(tmpdir):
    # Create a sample DataFrame
    data = {'A': [1, 2, None], 'B': [None, 4, 5]}
    df = pd.DataFrame(data)

    # Define filename and output directory
    filename = 'test_file.json'
    output_dir = str(tmpdir)

    # Call the function
    result_path = task_func(df, filename, output_dir)

    # Check if the file was created in the correct path
    assert os.path.exists(result_path)

    # Read the content of the file
    with open(result_path, 'r') as f:
        content = f.read()

    # Load the JSON content
    json_content = json.loads(content)

    # Expected JSON content
    expected_content = [
        {"A": 1, "B": None},
        {"A": 2, "B": 4},
        {"A": None, "B": 5}
    ]

    # Assert the content is as expected
    assert json_content == expected_content

def test_task_func_nonexistent_output_dir(tmpdir):
    # Create a sample DataFrame
    data = {'A': [1, 2, None], 'B': [None, 4, 5]}
    df = pd.DataFrame(data)

    # Define filename and output directory
    filename = 'test_file.json'
    output_dir = str(tmpdir.join('nonexistent_dir'))

    # Call the function
    result_path = task_func(df, filename, output_dir)

    # Check if the file was created in the correct path
    assert os.path.exists(result_path)

    # Read the content of the file
    with open(result_path, 'r') as f:
        content = f.read()

    # Load the JSON content
    json_content = json.loads(content)

    # Expected JSON content
    expected_content = [
        {"A": 1, "B": None},
        {"A": 2, "B": 4},
        {"A": None, "B": 5}
    ]

    # Assert the content is as expected
    assert json_content == expected_content