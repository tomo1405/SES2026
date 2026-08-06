import pytest
import requests
from src_0171 import task_func


def test_task_func():
    csv_url = "https://example.com/data.csv"
    sort_by_column = "title"
    expected_result = ...  # Replace with the expected result of the function
    result = task_func(csv_url, sort_by_column)
    assert result.equals(expected_result)

def test_task_func_with_invalid_csv_url():
    csv_url = "https://example.com/invalid_data.csv"
    sort_by_column = "title"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(csv_url, sort_by_column)

def test_task_func_with_invalid_sort_by_column():
    csv_url = "https://example.com/data.csv"
    sort_by_column = "invalid_column"
    with pytest.raises(ValueError):
        task_func(csv_url, sort_by_column)