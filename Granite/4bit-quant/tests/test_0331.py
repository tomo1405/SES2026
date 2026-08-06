import heapq
import random
import pytest

def task_func(list_length:5, k:int):
    numbers = [random.randint(0, 100) for _ in range(list_length)]
    heapq.heapify(numbers)
    largest_numbers = heapq.nlargest(k, numbers)
    return numbers, largest_numbers

def test_task_func():
    list_length = 5
    k = 3
    expected_output = ([42, 68, 76, 92, 95], [95, 92, 76])
    actual_output = task_func(list_length, k)
    assert actual_output == expected_output, "Output does not match expected output"

test_task_func()