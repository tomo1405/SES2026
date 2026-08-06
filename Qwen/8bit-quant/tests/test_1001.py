import json
import os

import pandas as pd
import pytest
from src_1001 import task_func


@pytest.fixture(autouse=True)
def cleanup():
    """Cleanup downloaded file after each test."""
    yield
    if os.path.exists("downloaded_file.json"):
        os.remove("downloaded_file.json")

def test_task_func_valid_url():
    url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province-latest.json"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_task_func_invalid_url():
    url = "https://example.com/nonexistentfile.json"
    with pytest.raises(json.JSONDecodeError):
        task_func(url)

def test_task_func_non_json_response():
    url = "https://httpbin.org/html"  # Returns HTML content
    with pytest.raises(json.JSONDecodeError):
        task_func(url)