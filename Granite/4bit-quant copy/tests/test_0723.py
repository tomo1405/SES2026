import pytest
import urllib.request
import os
import re
from src_0723 import task_func

def test_task_func():
    url = "https://example.com"
    occurrences = task_func(url)
    assert isinstance(occurrences, int)
    assert occurrences >= 0

def test_task_func_with_error():
    url = "https://example.com"
    with pytest.raises(Exception):
        task_func(url)

def test_task_func_with_invalid_url():
    url = "invalid_url"
    with pytest.raises(ValueError):
        task_func(url)