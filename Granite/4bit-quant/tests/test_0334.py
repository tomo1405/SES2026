import heapq
import random
import pytest

def task_func(k, list_length = 5, min_value = 0, max_value = 100):
    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    heapq.heapify(numbers)
    smallest_numbers = heapq.nsmallest(k, numbers)
    return numbers, smallest_numbers

def test_task_func():
    k = 3
    list_length = 10
    min_value = 0
    max_value = 100
    expected_output = ([56, 60, 61, 72, 87], [56, 60, 61])
    
    actual_output = task_func(k, list_length, min_value, max_value)
    
    assert actual_output == expected_output, "Output does not match expected output"

if __name__ == "__main__":
    pytest.main()