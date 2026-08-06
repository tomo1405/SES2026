python
import numpy as np
import string
import pytest

from src_0826 import task_func

def test_task_func():
    # Test case 1: length=4, seed=None, alphabets=list(string.ascii_lowercase)
    result = task_func(4, seed=None, alphabets=list(string.ascii_lowercase))
    assert len(result) == 10
    assert all(isinstance(x, str) for x in result)
    assert all(len(x) == 4 for x in result)
    assert all(x in string.ascii_lowercase for x in result)

    # Test case 2: length=5, seed=123, alphabets=['a', 'b', 'c']
    result = task_func(5, seed=123, alphabets=['a', 'b', 'c'])
    assert len(result) == 10
    assert all(isinstance(x, str) for x in result)
    assert all(len(x) == 5 for x in result)
    assert all(x in ['a', 'b', 'c'] for x in result)

    # Test case 3: length=3, seed=456, alphabets=['d', 'e', 'f', 'g']
    result = task_func(3, seed=456, alphabets=['d', 'e', 'f', 'g'])
    assert len(result) == 10
    assert all(isinstance(x, str) for x in result)
    assert all(len(x) == 3 for x in result)
    assert all(x in ['d', 'e', 'f', 'g'] for x in result)

    # Test case 4: length=2, seed=789, alphabets=['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    result = task_func(2, seed=789, alphabets=['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'])
    assert len(result) == 10
    assert all(isinstance(x, str) for x in result)
    assert all(len(x) == 2 for x in result)
    assert all(x in ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'] for x in result)

    # Test case 5: length=1, seed=101112, alphabets=['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = task_func(1, seed=101112, alphabets=['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    assert len(result) == 10
    assert all(isinstance(x, str) for x in result)
    assert all(len(x) == 1 for x in result)
    assert all(x in ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] for x in result)