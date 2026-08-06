import pytest
from src_0331 import task_func

def test_task_func():
    list_length = 10
    k = 3
    numbers, largest_numbers = task_func(list_length, k)
    
    # Check that the length of numbers is correct
    assert len(numbers) == list_length
    
    # Check that numbers is a heap
    assert all(numbers[i] <= numbers[2*i+1] and numbers[i] <= numbers[2*i+2] for i in range((list_length-2)//2))
    
    # Check that largest_numbers contains the k largest elements from numbers
    assert set(largest_numbers) == set(heapq.nlargest(k, numbers))
    
    # Check that the length of largest_numbers is correct
    assert len(largest_numbers) == k
    
    # Check that largest_numbers is sorted in descending order
    assert largest_numbers == sorted(largest_numbers, reverse=True)

# Test with edge cases
def test_task_func_edge_cases():
    # Test with k = 0
    list_length = 5
    k = 0
    numbers, largest_numbers = task_func(list_length, k)
    assert largest_numbers == []
    
    # Test with k = 1
    list_length = 5
    k = 1
    numbers, largest_numbers = task_func(list_length, k)
    assert len(largest_numbers) == 1
    assert largest_numbers[0] == max(numbers)
    
    # Test with k equal to list_length
    list_length = 5
    k = list_length
    numbers, largest_numbers = task_func(list_length, k)
    assert set(largest_numbers) == set(numbers)
    assert largest_numbers == sorted(numbers, reverse=True)
    
    # Test with k greater than list_length
    list_length = 5
    k = 6
    numbers, largest_numbers = task_func(list_length, k)
    assert set(largest_numbers) == set(numbers)
    assert largest_numbers == sorted(numbers, reverse=True)