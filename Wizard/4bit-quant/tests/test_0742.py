python
import pytest
from src_0742 import task_func

def test_task_func():
    my_dict = {'apple': 10, 'banana': 20, 'cherry': 30, 'date': 40}
    expected_result = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
    assert task_func(my_dict) == expected_result