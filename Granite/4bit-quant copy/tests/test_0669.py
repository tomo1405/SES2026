import pytest
from src_0669 import task_func

def test_task_func():
    assert task_func("abcd") == ['a', 'b', 'c', 'd']
    assert task_func("abracadabra") == ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
    assert task_func("aaaa") == ['a', 'a', 'a', 'a']
    assert task_func("abc") == ['a', 'b', 'c']