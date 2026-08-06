import random
import numpy as np
from src_0004 import task_func

def test_task_func():
    # Test case 1: empty input
    assert task_func([]) == {}

    # Test case 2: one element in input
    assert task_func(['A']) == {'A': 50.0}

    # Test case 3: multiple elements in input
    assert task_func(['A', 'B', 'C']) == {'A': 50.0, 'B': 50.0, 'C': 50.0}

    # Test case 4: input with different lengths
    assert task_func(['A', 'B', 'C', 'D']) == {'A': 50.0, 'B': 50.0, 'C': 50.0, 'D': 50.0}

    # Test case 5: input with different lengths and values
    assert task_func(['A', 'B', 'C', 'D', 'E']) == {'A': 50.0, 'B': 50.0, 'C': 50.0, 'D': 50.0, 'E': 50.0}