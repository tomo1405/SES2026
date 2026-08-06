python
import re
import random
import string

def task_func(n, pattern, seed=None):
    if seed is not None:
        random.seed(seed)
    rand_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    matches = re.findall(pattern, rand_str)
    return matches

def test_task_func():
    # Test case 1
    assert task_func(10, r'\d{3}') == ['123', '456', '789']

    # Test case 2
    assert task_func(10, r'\d{3}', 123) == ['123', '456', '789']

    # Test case 3
    assert task_func(10, r'\d{3}', 456) == ['456', '789', '123']

    # Test case 4
    assert task_func(10, r'\d{3}', 789) == ['789', '123', '456']

    # Test case 5
    assert task_func(10, r'\d{3}', 1234) == ['123', '456', '789']

    # Test case 6
    assert task_func(10, r'\d{3}', 4567) == ['456', '789', '123']

    # Test case 7
    assert task_func(10, r'\d{3}', 7891) == ['789', '123', '456']

    # Test case 8
    assert task_func(10, r'\d{3}', 12345) == ['123', '456', '789']

    # Test case 9
    assert task_func(10, r'\d{3}', 45678) == ['456', '789', '123']

    # Test case 10
    assert task_func(10, r'\d{3}', 78912) == ['789', '123', '456']