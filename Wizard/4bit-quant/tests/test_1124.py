python
import pytest
from src_1124 import task_func

def test_task_func():
    myString = "Here are some URLs: https://www.google.com, https://www.yahoo.com, and https://www.bing.com. Also, https://www.python.org is not a valid URL."
    expected_result = {'www.google.com': '2022-05-18T12:00:00', 'www.yahoo.com': '2022-05-18T12:00:00', 'www.bing.com': '2022-05-18T12:00:00'}
    assert task_func(myString) == expected_result