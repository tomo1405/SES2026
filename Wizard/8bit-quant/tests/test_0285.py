python
import pytest
from src_0285 import task_func

def test_task_func():
    url = 'https://www.example.com'
    links = task_func(url)
    assert len(links) > 0
    assert isinstance(links, list)
    assert all(isinstance(link, str) for link in links)