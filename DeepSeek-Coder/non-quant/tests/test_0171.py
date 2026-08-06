import pytest
from src_0171 import task_func
import pandas as pd
import requests
from io import StringIO

def test_task_func():
    # Test with a sample CSV URL
    csv_url = "https://example.com/sample.csv"
    response_mock = requests.Response()
    response_mock.status_code = 200
    response_mock._content = b'title,year\nTitle1,2020\nTitle2,2021\n'
    requests.get = lambda url: response_mock

    sorted_df = task_func(csv_url=csv_url)

    # Check the output
    assert sorted_df['title'].tolist() == ['Title1', 'Title2']
    assert sorted_df['year'].tolist() == [2020, 2021]