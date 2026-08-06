python
import random
from collections import Counter
import pytest

def task_func(strings: list) -> dict:
    if not strings:
        return Counter()

    pattern = '}'
    random_choices = random.choices(strings, k=10)
    pattern_counts = Counter([string.count(pattern) for string in random_choices])

    return pattern_counts

def test_task_func():
    # Test case 1: empty list
    assert task_func([]) == Counter()

    # Test case 2: list with one string
    assert task_func(['a{b}c']) == Counter({1: 1})

    # Test case 3: list with multiple strings
    strings = ['a{b}c', 'd{e}f', 'g{h}i', 'j{k}l', 'm{n}o', 'p{q}r', 's{t}u', 'v{w}x', 'y{z}a', 'b{c}d']
    expected_counts = Counter({1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2})
    assert task_func(strings) == expected_counts