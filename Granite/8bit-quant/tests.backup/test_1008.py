import pytest
import requests
import pandas as pd
from src_1008 import task_func

@pytest.mark.parametrize("url, expected_output", [
    ("https://jsonplaceholder.typicode.com/todos/1", pd.DataFrame({"userId": [1], "id": [1], "title": ["delectus aut autem"], "completed": [False]})),
    ("https://jsonplaceholder.typicode.com/todos/2", pd.DataFrame({"userId": [1], "id": [2], "title": ["quis ut distinctio"], "completed": [True]})),
])
def test_task_func(url, expected_output):
    """
    Test the task_func function with different input URLs and expected outputs.
    """
    df = task_func(url)
    assert df.equals(expected_output)

def test_task_func_invalid_url():
    """
    Test the task_func function with an invalid URL and check if it raises an exception.
    """
    with pytest.raises(SystemError, match="Network error occurred:"):
        task_func("https://invalid-url.com")

def test_task_func_invalid_json():
    """
    Test the task_func function with a URL that returns invalid JSON and check if it raises a ValueError.
    """
    with pytest.raises(ValueError, match="Invalid JSON format for DataFrame conversion"):
        task_func("https://jsonplaceholder.typicode.com/todos")