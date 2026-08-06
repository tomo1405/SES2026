python
import pytest
from src_1124 import task_func

def test_task_func():
    myString = "Here are some URLs: https://www.google.com, https://www.facebook.com, and https://www.twitter.com"
    expected_output = {'www.google.com': '20220518000000Z', 'www.facebook.com': '20220518000000Z', 'www.twitter.com': '20220518000000Z'}
    assert task_func(myString) == expected_output