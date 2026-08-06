import pandas as pd
import pytest
import requests
from src_0391 import task_func


def test_task_func_valid_input():
    csv_url_dict = {"URL": "https://example.com/data.csv"}
    expected_df = pd.DataFrame({"title": ["Title 1", "Title 2", "Title 3"], "author": ["Author 1", "Author 2", "Author 3"]})
    actual_df = task_func(csv_url_dict)
    assert actual_df.equals(expected_df)

def test_task_func_invalid_input():
    csv_url_dict = {"URL": "https://example.com/data.csv", "invalid_key": "invalid_value"}
    with pytest.raises(ValueError):
        task_func(csv_url_dict)

def test_task_func_invalid_url():
    csv_url_dict = {"URL": "https://example.com/invalid_data.csv"}
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(csv_url_dict)