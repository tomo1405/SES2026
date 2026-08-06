python
import pytest
from src_1109 import task_func

def test_task_func():
    result = [
        {'http://www.google.com': 'Google', 'https://www.facebook.com': 'Facebook'},
        {'http://www.yahoo.com': 'Yahoo', 'https://www.bing.com': 'Bing'},
        {'http://www.wikipedia.org': 'Wikipedia', 'https://www.twitter.com': 'Twitter'}
    ]
    expected_output = {'http://www.google.com': 'Google', 'https://www.facebook.com': 'Facebook'}
    assert task_func(result) == expected_output