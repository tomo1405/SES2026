import pytest
from src_0848 import task_func
import os
import string
import random

def test_task_func():
    # Mocking the random.randint function to ensure predictable filenames
    class MockRandom:
        def randint(self, a, b):
            return 12345  # Fixed random number for testing

    random_mock = MockRandom()
    original_random = random.random
    random.random = random_mock.randint

    input_string = "Hello, world!\nThis is a test."
    expected_filenames = ['12345.txt', '12345.txt']
    expected_directory = './text_files'

    # Ensure the directory exists
    os.makedirs(expected_directory, exist_ok=True)

    # Call the function
    result = task_func(input_string, directory=expected_directory)

    # Check if the correct number of files were created
    assert len(result) == len(expected_filenames)

    # Check if the file paths are correct
    for i, filepath in enumerate(result):
        assert os.path.join(expected_directory, expected_filenames[i]) == filepath

    # Check the contents of the files
    with open(result[0], 'r') as file:
        content = file.read()
        assert content == "Hello world"

    with open(result[1], 'r') as file:
        content = file.read()
        assert content == "This is a test"

    # Clean up the created files
    for filepath in result:
        os.remove(filepath)

    # Restore the original random function
    random.random = original_random