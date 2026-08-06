import pytest
from src_0123 import task_func

def test_task_func_appends_random_number():
    original_list = [1, 2, 3]
    result = task_func(original_list.copy())
    
    # Check that the list has one more element than before
    assert len(result) == len(original_list) + 1
    
    # Check that the last element is within the expected range
    assert 0 <= result[-1] <= 100

def test_task_func_returns_numpy_array():
    original_list = [1, 2, 3]
    result = task_func(original_list.copy())
    
    # Check that the result is a numpy array
    assert isinstance(result, np.ndarray)

def test_task_func_array_size():
    original_list = [1, 2, 3]
    result = task_func(original_list.copy())
    
    # Calculate the expected size of the array
    expected_size = sum(original_list) + result[-1]
    
    # Check that the size of the array matches the expected size
    assert result.size == expected_size

def test_task_func_array_values():
    original_list = [1, 2, 3]
    result = task_func(original_list.copy())
    
    # Check that all values in the array are between 0 and 1
    assert np.all(result >= 0)
    assert np.all(result <= 1)