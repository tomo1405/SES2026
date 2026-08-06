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
        os.path.join(DIRECTORY, "7d403e01c506a8d2a1367c801977c5ad.txt"),
    ]
    assert task_func(input_string) == expected_output

    # Test case 2
    input_string = "Hello\nWorld\n\n"
    expected_output = [
        os.path.join(DIRECTORY, "5eb63bbbe01eeed093cb22bb8f5acdc3.txt"),
        os.path.join(DIRECTORY, "7d403e01c506a8d2a1367c801977c5ad.txt"),
        os.path.join(DIRECTORY, "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.txt"),
    ]
    assert task_func(input_string) == expected_output

    # Test case 3
    input_string = ""
    expected_output = []
    assert task_func(input_string) == expected_output

    # Test case 4
    input_string = "Hello\nWorld\n\n\n"
    expected_output = [
        os.path.join(DIRECTORY, "5eb63bbbe01eeed093cb22bb8f5acdc3.txt"),
        os.path.join(DIRECTORY, "7d403e01c506a8d2a1367c801977c5ad.txt"),
        os.path.join(DIRECTORY, "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.txt"),
        os.path.join(DIRECTORY, "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.txt"),
    ]
    assert task_func(input_string) == expected_output

if __name__ == "__main__":
    test_task_func()