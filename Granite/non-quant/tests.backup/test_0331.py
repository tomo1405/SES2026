import heapq
import random
import pytest
from src_0331 import task_func

def test_task_func():
    list_length = 5
    k = 3
    numbers, largest_numbers = task_func(list_length, k)
    assert len(largest_numbers) == k
    assert all(number in numbers for number in largest_numbers)
    assert heapq.nlargest(k, numbers) == largest_numbers