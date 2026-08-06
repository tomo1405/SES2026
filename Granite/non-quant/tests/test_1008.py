import pandas as pd
import pytest
from src_1008 import task_func


def test_task_func():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    expected_df = pd.DataFrame({"userId": [1], "id": [1], "title": ["delectus aut autem"], "completed": [False]})

    df = task_func(url)
    assert df.equals(expected_df)

def test_task_func_with_invalid_url():
    url = "https://jsonplaceholder.typicode.com/invalid_url"
    with pytest.raises(SystemError, match="Network error occurred:"):
        task_func(url)

def test_task_func_with_invalid_json():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    invalid_json = '{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}'
    with pytest.raises(ValueError, match="Invalid JSON format for DataFrame conversion"):
        task_func(url, data=invalid_json)