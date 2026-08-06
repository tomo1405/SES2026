python
import heapq
import random
import pytest

def task_func(list_length:int, k:int):
    numbers = [random.randint(0, 100) for _ in range(list_length)]
    heapq.heapify(numbers)
    largest_numbers = heapq.nlargest(k, numbers)
    return numbers, largest_numbers

def test_task_func():
    # Test case 1
    list_length = 10
    k = 5
    numbers, largest_numbers = task_func(list_length, k)
    assert len(numbers) == list_length
    assert len(largest_numbers) == k
    assert all(num in numbers for num in largest_numbers)
    assert all(num <= largest_numbers[0] for num in largest_numbers)

    # Test case 2
    list_length = 100
    k = 10
    numbers, largest_numbers = task_func(list_length, k)
    assert len(numbers) == list_length
    assert len(largest_numbers) == k
    assert all(num in numbers for num in largest_numbers)
    assert all(num <= largest_numbers[0] for num in largest_numbers)

    # Test case 3
    list_length = 1000
    k = 100
    numbers, largest_numbers = task_func(list_length, k)
    assert len(numbers) == list_length
    assert len(largest_numbers) == k
    assert all(num in numbers for num in largest_numbers)
    assert all(num <= largest_numbers[0] for num in largest_numbers)