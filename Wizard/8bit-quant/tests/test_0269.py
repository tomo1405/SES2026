python
import collections
import random
import pytest

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def task_func(n_keys, n_values):

    keys = [random.choice(LETTERS) for _ in range(n_keys)]
    values = list(range(1, n_values + 1))
    return dict(collections.OrderedDict((k, values) for k in keys))

def test_task_func():
    # Test case 1
    assert task_func(3, 5) == {'a': [1, 2, 3, 4, 5], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4, 5]}

    # Test case 2
    assert task_func(2, 3) == {'a': [1, 2, 3], 'b': [1, 2, 3]}

    # Test case 3
    assert task_func(1, 1) == {'a': [1]}

    # Test case 4
    assert task_func(0, 0) == {}

    # Test case 5
    with pytest.raises(ValueError):
        task_func(-1, 1)

    # Test case 6
    with pytest.raises(ValueError):
        task_func(1, -1)