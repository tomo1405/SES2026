import pytest
from src_0863 import task_func

def test_task_func():
    n = 10
    seed = 1234
    letter_dict = task_func(n, seed)
    assert len(letter_dict) == n
    assert all(len(v) == 1 for v in letter_dict.values())
    assert all(k in string.ascii_lowercase for k in letter_dict.keys())
    assert all(v[0] == k for k, v in letter_dict.items())