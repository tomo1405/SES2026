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
    table_id = "example_table"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(url, table_id)

def test_task_func_table_not_found():
    url = "https://www.example.com"
    table_id = "nonexistent_table"
    with pytest.raises(ValueError, match="Table with the specified ID not found."):
        task_func(url, table_id)

def test_task_func_empty_table():
    url = "https://www.example.com"
    table_id = "empty_table"
    df = task_func(url, table_id)
    assert df.empty