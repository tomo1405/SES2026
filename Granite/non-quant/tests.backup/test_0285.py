import pytest
from src_0285 import task_func

def test_task_func():
    url = "https://www.example.com"
    links = task_func(url)
    assert isinstance(links, list)
    assert all(isinstance(link, str) for link in links)

def test_task_func_with_invalid_url():
    with pytest.raises(ValueError):
        task_func("invalid_url")