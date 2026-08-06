python
import os
import hashlib
import pytest

# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    file_paths = []
    lines = input_string.split("\n")
    for line in lines:
        if line:  # Check if line is not empty
            line_hash = hashlib.sha256(line.encode()).hexdigest()
            filename = line_hash[:10] + ".txt"
            filepath = os.path.join(DIRECTORY, filename)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(line_hash)
            file_paths.append(filepath)

    return file_paths

def test_task_func():
    # Test case 1
    input_string = "Hello\nWorld\n"
    expected_output = [
        os.path.join(DIRECTORY, "5eb63bbbe01eeed093cb22bb8f5acdc3.txt"),
        os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"),
    ]
    assert task_func(input_string) == expected_output

    # Test case 2
    input_string = "This is a test string\n"
    expected_output = [
        os.path.join(DIRECTORY, "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3.txt"),
    ]
    assert task_func(input_string) == expected_output

    # Test case 3
    input_string = ""
    expected_output = []
    assert task_func(input_string) == expected_output