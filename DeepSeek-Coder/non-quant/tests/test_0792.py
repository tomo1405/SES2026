import pytest
from src_0792 import task_func
from collections import Counter
import random
from itertools import cycle

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def test_task_func():
    # Test case 1: Non-empty list
    random.seed(42)  # Seed for reproducibility
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    result = task_func(l)
    assert isinstance(result, Counter)
    assert len(result) == 3

    # Test case 2: Empty list
    empty_list = []
    result = task_func(empty_list)
    assert isinstance(result, Counter)
    assert len(result) == 0

    # Additional test cases can be added here

if __name__ == "__main__":
    pytest.main()