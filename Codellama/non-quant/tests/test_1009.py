import pytest
import requests
from src_1009 import task_func


def test_task_func_valid_url():
    url = "https://www.example.com"
    table_id = "table_id"
    df = task_func(url, table_id)
    assert isinstance(df, pd.DataFrame)

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid"
    table_id = "table_id"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(url, table_id)

def test_task_func_invalid_table_id():
    url = "https://www.example.com"
    table_id = "invalid_table_id"
    with pytest.raises(ValueError):
        task_func(url, table_id)

def test_task_func_empty_table():
    url = "https://www.example.com"
    table_id = "table_id"
    df = task_func(url, table_id)
    assert df.empty