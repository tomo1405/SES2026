python
import heapq
import random
import pytest

def task_func(list_length:5, k:int):
    numbers = [random.randint(0, 100) for _ in range(list_length)]
    heapq.heapify(numbers)
    largest_numbers = heapq.nlargest(k, numbers)
    return numbers, largest_numbers

def test_task_func():
    # Test case 1
    numbers, largest_numbers = task_func(list_length=5, k=3)
    assert numbers == [99, 98, 97, 96, 95]
    assert largest_numbers == [99, 98, 97]

    # Test case 2
    numbers, largest_numbers = task_func(list_length=10, k=5)
    assert numbers == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
    assert largest_numbers == [99, 98, 97, 96, 95]

    # Test case 3
    numbers, largest_numbers = task_func(list_length=10, k=10)
    assert numbers == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
    assert largest_numbers == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]

    # Test case 4
    numbers, largest_numbers = task_func(list_length=10, k=0)
    assert numbers == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
    assert largest_numbers == []

    # Test case 5
    numbers, largest_numbers = task_func(list_length=10, k=1)
    assert numbers == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
    assert largest_numbers == [99]

    # Test case 6
    numbers, largest_numbers = task_func(list_length=10, k=100)
    assert numbers == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]
    assert largest_numbers == [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]