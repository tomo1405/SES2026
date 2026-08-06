import pytest
from src_0724 import task_func

def test_task_func():
    url = 'http://example.com'
    result = task_func(url)
    assert result == 'scraped_data.csv'