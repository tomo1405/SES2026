import pytest
from src_0331 import task_func

def test_task_func():
    # Test with default list length and k
    list_length = 10
    k = 3
    numbers, largest_numbers = task_func(list_length, k)
    
    # Check if the length of the generated list is correct
    assert len(numbers) == list_length
    
    # Check if the list is a valid heap
    assert all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    
    # Check if the largest_numbers are indeed the k largest elements
    assert sorted(largest_numbers, reverse=True) == sorted(numbers)[-k:]
    
    # Test with k equal to list_length
    k = list_length
    numbers, largest_numbers = task_func(list_length, k)
    assert largest_numbers == sorted(numbers, reverse=True)
    
    # Test with k greater than list_length (should return the entire list sorted)
    k = list_length + 5
    numbers, largest_numbers = task_func(list_length, k)
    assert largest_numbers == sorted(numbers, reverse=True)

# Test with edge cases
def test_edge_cases():
    # Test with list_length = 1 and k = 1
    list_length = 1
    k = 1
    numbers, largest_numbers = task_func(list_length, k)
    assert len(numbers) == list_length
    assert largest_numbers == numbers
    
    # Test with k = 0 (should return an empty list)
    k = 0
    numbers, largest_numbers = task_func(list_length, k)
    assert largest_numbers == []