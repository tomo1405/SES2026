import pytest
from src_0721 import task_func

def test_task_func():
    # Call the function and capture the output
    result = task_func()
    
    # Add assertions to verify the output
    assert isinstance(result, str), "The function should return a file path as a string."
    assert os.path.isfile(result), "The file should be created."
    assert os.path.getsize(result) > 0, "The file should not be empty."