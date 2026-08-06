import pytest
from src_0123 import task_func

def test_task_func():
    # Test with an empty list
    my_list = []
    result = task_func(my_list)
    assert isinstance(result, np.ndarray)
    assert len(result) == my_list[0]  # The length of the array should be the first element in the list, which is the random number appended

    # Test with a non-empty list
    my_list = [5]
    result = task_func(my_list)
    assert isinstance(result, np.ndarray)
    assert len(result) == my_list[0]  # The length of the array should be the first element in the list, which is the random number appended

    # Test with a list containing negative numbers (should be treated as zero for size calculation)
    my_list = [-1, -2, -3]
    result = task_func(my_list)
    assert isinstance(result, np.ndarray)
    assert len(result) == 0  # The length of the array should be zero since the sum of negative numbers is zero

    # Test with a list containing large positive numbers
    my_list = [1000, 2000, 3000]
    result = task_func(my_list)
    assert isinstance(result, np.ndarray)
    assert len(result) == my_list[0]  # The length of the array should be the first element in the list, which is the random number appended

    # Test with a list containing a mix of positive and negative numbers
    my_list = [10, -5, 20]
    result = task_func(my_list)
    assert isinstance(result, np.ndarray)
    assert len(result) == my_list[0]  # The length of the array should be the first element in the list, which is the random number appended