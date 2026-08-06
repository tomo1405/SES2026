import pytest
from src_0591 import task_func

def test_task_func_valid_url():
    url = "http://example.com"
    result = task_func(url)
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0
    assert 'text' in result.columns
    assert 'href' in result.columns
    assert 'fetch_time' in result.columns

def test_task_func_invalid_url():
    url = ""
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_network_error():
    url = "http://invalid-url.com"
    with pytest.raises(urllib.error.URLError):
        task_func(url)