python
import heapq
import random
import pytest

def task_func(k, list_length=5, min_value=0, max_value=100):
    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    heapq.heapify(numbers)
    smallest_numbers = heapq.nsmallest(k, numbers)
    return numbers, smallest_numbers

def test_task_func():
    numbers, smallest_numbers = task_func(3)
    assert len(numbers) == 5
    assert len(smallest_numbers) == 3
    assert all(isinstance(n, int) for n in numbers)
    assert all(isinstance(n, int) for n in smallest_numbers)
    assert all(n >= 0 and n <= 100 for n in numbers)
    assert all(n >= 0 and n <= 100 for n in smallest_numbers)
    assert all(n in numbers for n in smallest_numbers)