import pytest
import urllib.request
import os
import json
import pandas as pd
from src_1001 import task_func

def test_task_func_valid_url():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)

def test_task_func_invalid_url():
    url = "https://jsonplaceholder.typicode.com/invalid_url"
    with pytest.raises(urllib.error.URLError):
        task_func(url)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_file_not_found():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    df = task_func(url)
    assert os.path.exists(TARGET_JSON_FILE) == False