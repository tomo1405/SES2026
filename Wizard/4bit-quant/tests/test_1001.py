python
import urllib.request
import os
import json
import pandas as pd
import pytest

# Constants
TARGET_JSON_FILE = "downloaded_file.json"

def task_func(url):
    urllib.request.urlretrieve(url, TARGET_JSON_FILE)

    with open(TARGET_JSON_FILE, "r") as f:
        data = json.load(f)

    os.remove(TARGET_JSON_FILE)

    return pd.DataFrame(data)

def test_task_func():
    # Test case 1: Valid URL
    url = "https://jsonplaceholder.typicode.com/todos/1"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 5)
    assert df.iloc[0]["userId"] == 1
    assert df.iloc[0]["id"] == 1
    assert df.iloc[0]["title"] == "delectus aut autem"
    assert df.iloc[0]["completed"] == False

    # Test case 2: Invalid URL
    url = "https://jsonplaceholder.typicode.com/todos/1000"
    with pytest.raises(urllib.error.HTTPError):
        task_func(url)