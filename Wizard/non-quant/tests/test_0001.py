python
import itertools
import random
import pytest

from src_0001 import task_func

def test_task_func():
    # Test default input
    assert task_func() == 1.0
    
    # Test custom input
    assert task_func([1, 2, 3]) == 1.0
    
    # Test edge cases
    assert task_func([1]) == 0.0
    assert task_func([1, 1]) == 0.0
    assert task_func([1, 2, 1]) == 0.0
    
    # Test random input
    for i in range(100):
        numbers = [random.randint(1, 10) for j in range(random.randint(1, 10))]
        assert task_func(numbers) >= 0.0