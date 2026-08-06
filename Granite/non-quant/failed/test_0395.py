import pytest
from src_0395 import task_func
import collections
import string
import random

def test_task_func():
    # Test case 1: Test with default seed and length
    random.seed(0)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    char_freq = collections.Counter(random_string)
    expected_output = dict(char_freq)
    actual_output = task_func(10)
    assert actual_output == expected_output

    # Test case 2: Test with custom seed and length
    random.seed(123)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(20))
    char_freq = collections.Counter(random_string)
    expected_output = dict(char_freq)
    actual_output = task_func(20, 123)
    assert actual_output == expected_output

    # Test case 3: Test with zero length
    with pytest.raises(ValueError):
        task_func(0)

    # Test case 4: Test with negative length
    with pytest.raises(ValueError):
        task_func(-10)