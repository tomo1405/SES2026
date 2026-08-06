import pytest
from src_0848 import task_func
import os
import string
import random

def test_task_func():
    # Mocking the random.randint function to control the filename generation
    random_mock = random.Random()
    random_mock.seed(42)  # Ensure reproducibility
    random.randint = random_mock.randint

    # Create a temporary directory for testing
    temp_dir = 'temp_test_dir'
    os.makedirs(temp_dir, exist_ok=True)

    # Define test inputs
    input_string = "Hello, World!\nThis is a test."
    expected_filenames = [
        f"{random.randint(10000, 99999)}.txt",
        f"{random.randint(10000, 99999)}.txt"
    ]

    # Call the function
    result = task_func(input_string, directory=temp_dir)

    # Check if the returned file paths match the expected pattern
    assert len(result) == 2
    for i, path in enumerate(result):
        assert os.path.basename(path) == expected_filenames[i]
        assert os.path.exists(path)

    # Check the content of the files
    with open(result[0], 'r') as file:
        content = file.read()
        assert content == "Hello World"

    with open(result[1], 'r') as file:
        content = file.read()
        assert content == "This is a test"

    # Clean up the temporary directory
    for file_path in result:
        os.remove(file_path)
    os.rmdir(temp_dir)