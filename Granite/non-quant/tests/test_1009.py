import pytest
import requests
from src_1009 import task_func


def test_task_func_valid_input():
    url = "https://www.example.com"
    table_id = "example_table"
    df = task_func(url, table_id)
    assert isinstance(df, pd.DataFrame)

def test_task_func_http_error():
    url = "https://www.example.com"
    table_id = "nonexistent_table"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(url, table_id)

def test_task_func_value_error():
    url = "https://www.example.com"
    table_id = "empty_table"
    with pytest.raises(ValueError):
        task_func(url, table_id)