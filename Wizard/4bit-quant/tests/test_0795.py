python
import string
import random
import pytest

def task_func(length, random_seed=None):
    random.seed(random_seed)
    # Constants
    BRACKETS = "(){}[]"
    return ''.join(random.choice(string.ascii_lowercase + BRACKETS) for _ in range(length))

def test_task_func():
    # Test case 1
    assert task_func(10) == "h(a)b[c]d{e}f"
    
    # Test case 2
    assert task_func(5, 123) == "a[b]c{d}e"
    
    # Test case 3
    assert task_func(15, 456) == "a[b]c{d}e(f)g{h}i[j]k{l}m(n)o[p]q"