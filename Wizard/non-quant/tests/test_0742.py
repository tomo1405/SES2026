python
import pytest
from src_0742 import task_func

def test_task_func():
    my_dict = {'apple': 10, 'banana': 20, 'cherry': 30, 'date': 40, 'elderberry': 50}
    expected_result = {'a': 10, 'b': 30, 'c': 60, 'd': 90, 'e': 120}
    assert task_func(my_dict) == expected_result