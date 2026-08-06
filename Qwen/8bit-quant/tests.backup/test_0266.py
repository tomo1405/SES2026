import pytest
from src_0266 import task_func
import os
import json
import tempfile

def test_task_func():
    # Create a temporary directory to store the JSON file
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        # Sample input data
        data = {'b': 2, 'c': 3, 'd': 2}

        # Call the function
        json_file_path = task_func(data)

        # Check if the file was created
        assert os.path.exists(json_file_path)

        # Read the content of the JSON file
        with open(json_file_path, 'r') as json_file:
            content = json.load(json_file)

        # Check if the data was correctly written to the JSON file
        expected_data = {'b': 2, 'c': 3, 'd': 2, 'a': 1}
        assert content['data'] == expected_data

        # Check if the frequency was correctly calculated
        expected_freq = {2: 2, 3: 1, 1: 1}
        assert content['freq'] == expected_freq

def test_task_func_default_filename():
    # Create a temporary directory to store the JSON file
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        # Sample input data
        data = {'b': 2, 'c': 3, 'd': 2}

        # Call the function with default filename
        json_file_path = task_func(data)

        # Check if the file was created with the default name
        assert os.path.basename(json_file_path) == 'data.json'

def test_task_func_custom_filename():
    # Create a temporary directory to store the JSON file
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)

        # Sample input data
        data = {'b': 2, 'c': 3, 'd': 2}

        # Custom filename
        custom_filename = 'custom_data.json'

        # Call the function with a custom filename
        json_file_path = task_func(data, json_file_name=custom_filename)

        # Check if the file was created with the custom name
        assert os.path.basename(json_file_path) == custom_filename