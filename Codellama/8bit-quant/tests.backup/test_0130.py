import pytest
from src_0130 import task_func

def test_task_func_valid_url():
    url = "http://example.com"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0

def test_task_func_invalid_url():
    url = "http://example.com/invalid"
    with pytest.raises(ConnectionError):
        task_func(url)

def test_task_func_no_table():
    url = "http://example.com"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_no_data():
    url = "http://example.com"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_error_parsing():
    url = "http://example.com"
    with pytest.raises(ValueError):
        task_func(url)