from io import StringIO

import pandas as pd
import pytest
import requests
from src_0171 import task_func


def test_task_func_valid_csv_url():
    csv_url = "https://raw.githubusercontent.com/pytest-dev/pytest/main/tests/test_data/test_data.csv"
    sort_by_column = "title"
    expected_output = pd.read_csv(StringIO(response.text)).sort_values(by=sort_by_column)
    assert task_func(csv_url, sort_by_column).equals(expected_output)

def test_task_func_invalid_csv_url():
    csv_url = "https://raw.githubusercontent.com/pytest-dev/pytest/main/tests/test_data/invalid_data.csv"
    sort_by_column = "title"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(csv_url, sort_by_column)

def test_task_func_invalid_sort_by_column():
    csv_url = "https://raw.githubusercontent.com/pytest-dev/pytest/main/tests/test_data/test_data.csv"
    sort_by_column = "invalid_column"
    with pytest.raises(KeyError):
        task_func(csv_url, sort_by_column)