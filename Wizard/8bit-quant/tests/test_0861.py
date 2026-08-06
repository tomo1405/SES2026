python
import re
import random
import string
import pytest

def task_func(n, pattern, seed=None):
    if seed is not None:
        random.seed(seed)
    rand_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    matches = re.findall(pattern, rand_str)
    return matches

def test_task_func():
    # Test case 1: n=10, pattern='[a-z]+', seed=None
    assert task_func(10, '[a-z]+') == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']

    # Test case 2: n=10, pattern='[a-z]+', seed=123
    assert task_func(10, '[a-z]+', seed=123) == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']

    # Test case 3: n=10, pattern='[0-9]+', seed=None
    assert task_func(10, '[0-9]+') == ['4', '3', '2', '1', '9', '5', '8', '7', '6', '0']

    # Test case 4: n=10, pattern='[0-9]+', seed=123
    assert task_func(10, '[0-9]+', seed=123) == ['4', '3', '2', '1', '9', '5', '8', '7', '6', '0']

    # Test case 5: n=10, pattern='[a-zA-Z0-9]+', seed=None
    assert task_func(10, '[a-zA-Z0-9]+') == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']

    # Test case 6: n=10, pattern='[a-zA-Z0-9]+', seed=123
    assert task_func(10, '[a-zA-Z0-9]+', seed=123) == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']

    # Test case 7: n=10, pattern='[a-zA-Z]+', seed=None
    assert task_func(10, '[a-zA-Z]+') == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']

    # Test case 8: n=10, pattern='[a-zA-Z]+', seed=123
    assert task_func(10, '[a-zA-Z]+', seed=123) == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']

    # Test case 9: n=10, pattern='[a-zA-Z0-9]{5,}', seed=None
    assert task_func(10, '[a-zA-Z0-9]{5,}') == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']

    # Test case 10: n=10, pattern='[a-zA-Z0-9]{5,}', seed=123
    assert task_func(10, '[a-zA-Z0-9]{5,}', seed=123) == ['w', 'v', 'y', 's', 't', 'j', 'i', 'h', 'm', 'a']