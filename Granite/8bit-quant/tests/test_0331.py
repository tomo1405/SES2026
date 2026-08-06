import heapq
import random
import pytest

from src_0331 import task_func

def test_task_func():
    list_length = 5
    k = 3
    expected_output = ([42, 68, 76, 95, 100], [95, 100, 76])
    
    numbers = [random.randint(0, 100) for _ in range(list_length)]
    heapq.heapify(numbers)
    largest_numbers = heapq.nlargest(k, numbers)
    
    assert task_func(list_length, k) == expected_output