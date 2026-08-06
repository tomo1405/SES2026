import pytest
import urllib.request
import os
import json
import pandas as pd
# Constants
TARGET_JSON_FILE = "downloaded_file.json"
def task_func(url):
    urllib.request.urlretrieve(url, TARGET_JSON_FILE)

    with open(TARGET_JSON_FILE, "r") as f:
        data = json.load(f)

    os.remove(TARGET_JSON_FILE)

    return pd.DataFrame(data)
def test_task_func():
    url = "https://jsonplaceholder.typicode.com/posts"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert "userId" in df.columns
    assert "title" in df.columns
def test_task_func_invalid_url():
    url = "https://invalidurl.com/posts"
    with pytest.raises(Exception) as excinfo:
        task_func(url)
    assert "Unable to retrieve data from the given URL" in str(excinfo.value)