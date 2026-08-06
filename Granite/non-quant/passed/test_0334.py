import heapq
import random
import pytest

from src_0334 import task_func

def test_task_func():
    k = 3
    list_length = 5
    min_value = 0
    max_value = 100

    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)

    assert len(smallest_numbers) == k
    assert all(number in numbers for number in smallest_numbers)
    assert heapq.nsmallest(k, numbers) == smallest_numbers