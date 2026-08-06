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

# Test cases
def test_task_func_empty_string():
    assert task_func("") == []

def test_task_func_single_line():
    assert task_func("hello world") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

def test_task_func_multiple_lines():
    assert task_func("hello\nworld\n") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"), os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

def test_task_func_multiple_lines_with_empty_lines():
    assert task_func("hello\n\nworld\n\n") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"), os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

def test_task_func_multiple_lines_with_spaces():
    assert task_func("hello world\n  \n  world\n") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"), os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

def test_task_func_multiple_lines_with_special_chars():
    assert task_func("hello world\n!@#$%^&*()_+-=[]{}|;':\",./<>?\nworld\n") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"), os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

def test_task_func_multiple_lines_with_unicode():
    assert task_func("こんにちは\nこんばんは\n") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"), os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

def test_task_func_multiple_lines_with_unicode_and_spaces():
    assert task_func("こんにちは\n  \nこんばんは\n") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"), os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

def test_task_func_multiple_lines_with_unicode_and_special_chars():
    assert task_func("こんにちは\n!@#$%^&*()_+-=[]{}|;':\",./<>?\nこんばんは\n") == [os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt"), os.path.join(DIRECTORY, "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9.txt")]

# Run tests with pytest
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", __file__])