import pytest
from src_1051 import task_func
import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"

def test_task_func():
    # Test with a simple input string
    input_string = "hello\nworld"
    expected_filenames = [
        hashlib.sha256("hello".encode()).hexdigest()[:10] + ".txt",
        hashlib.sha256("world".encode()).hexdigest()[:10] + ".txt"
    ]
    expected_filepaths = [os.path.join(DIRECTORY, filename) for filename in expected_filenames]

    # Ensure the directory does not exist before running the test
    if os.path.exists(DIRECTORY):
        os.rmdir(DIRECTORY)

    # Run the function
    result = task_func(input_string)

    # Check if the directory was created
    assert os.path.exists(DIRECTORY)

    # Check if the correct files were created
    for filepath in expected_filepaths:
        assert filepath in result
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            assert content == hashlib.sha256("hello".encode()).hexdigest() if "hello" in filepath else hashlib.sha256("world".encode()).hexdigest()

    # Clean up after the test
    for filepath in expected_filepaths:
        os.remove(filepath)
    os.rmdir(DIRECTORY)

def test_task_func_empty_input():
    # Test with an empty input string
    input_string = ""
    expected_filepaths = []

    # Ensure the directory does not exist before running the test
    if os.path.exists(DIRECTORY):
        os.rmdir(DIRECTORY)

    # Run the function
    result = task_func(input_string)

    # Check if the directory was created
    assert os.path.exists(DIRECTORY)

    # Check if no files were created
    assert result == expected_filepaths

    # Clean up after the test
    os.rmdir(DIRECTORY)

def test_task_func_single_line():
    # Test with a single line input string
    input_string = "single_line"
    expected_filename = hashlib.sha256("single_line".encode()).hexdigest()[:10] + ".txt"
    expected_filepath = os.path.join(DIRECTORY, expected_filename)

    # Ensure the directory does not exist before running the test
    if os.path.exists(DIRECTORY):
        os.rmdir(DIRECTORY)

    # Run the function
    result = task_func(input_string)

    # Check if the directory was created
    assert os.path.exists(DIRECTORY)

    # Check if the correct file was created
    assert expected_filepath in result
    with open(expected_filepath, "r", encoding="utf-8") as file:
        content = file.read()
        assert content == hashlib.sha256("single_line".encode()).hexdigest()

    # Clean up after the test
    os.remove(expected_filepath)
    os.rmdir(DIRECTORY)