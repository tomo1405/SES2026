import urllib

import pytest
from src_0591 import task_func


def test_task_func():
    url = "https://www.example.com"
    df = task_func(url)
    assert df.shape == (10, 3)
    assert df.columns.tolist() == ['text', 'href', 'fetch_time']
    assert df.dtypes.tolist() == ['object', 'object', 'datetime64[ns]']
    assert df.iloc[0]['text'] == 'Example Domain'
    assert df.iloc[0]['href'] == 'https://www.iana.org/domains/example'
    assert df.iloc[0]['fetch_time'] == '2023-02-21 12:34:56'

def test_task_func_empty_url():
    url = ""
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_invalid_url():
    url = "https://www.example.com/invalid"
    with pytest.raises(urllib.error.URLError):
        task_func(url)