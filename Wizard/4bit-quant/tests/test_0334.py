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
    # Test case 1
    k = 3
    list_length = 5
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 2
    k = 10
    list_length = 10
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 3
    k = 5
    list_length = 10
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 4
    k = 10
    list_length = 5
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 5
    k = 1
    list_length = 10
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 6
    k = 10
    list_length = 1
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 7
    k = 1
    list_length = 1
    min_value = 0
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 8
    k = 1
    list_length = 10
    min_value = 100
    max_value = 200
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 9
    k = 10
    list_length = 10
    min_value = 100
    max_value = 200
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))

    # Test case 10
    k = 10
    list_length = 10
    min_value = 100
    max_value = 100
    numbers, smallest_numbers = task_func(k, list_length, min_value, max_value)
    assert len(numbers) == list_length
    assert len(smallest_numbers) == k
    assert all(smallest_numbers[i] <= smallest_numbers[j] for i in range(k-1) for j in range(i+1, k))