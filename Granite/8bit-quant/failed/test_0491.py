import pytest
from src_0491 import task_func

def test_task_func():
    s = "<xml>data</xml>"
    file_path = "output.json"
    expected_output = {"xml": "data"}

    # Test that the function returns the expected output
    assert task_func(s, file_path) == expected_output

    # Test that the JSON file was created and has the expected content
    with open(file_path, "r") as f:
        actual_output = json.load(f)
    assert actual_output == expected_output

    # Clean up the generated JSON file
    import os
    os.remove(file_path)