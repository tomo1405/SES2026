import pytest
from src_0596 import task_func
from array import array

def test_task_func_default_values():
    nums, pos = task_func()
    assert isinstance(nums, array)
    assert len(nums) == 10
    assert sum(nums) == 100
    assert 0 <= pos <= 10

def test_task_func_custom_values():
    n = 5
    total = 50
    nums, pos = task_func(n, total)
    assert isinstance(nums, array)
    assert len(nums) == n
    assert sum(nums) == total
    assert 0 <= pos <= n

def test_task_func_sum_not_reached():
    # This test checks if the function can handle cases where the initial sum is not reached
    def mock_random_int(a, b):
        return 0  # Always return 0 to simulate a case where sum is not reached

    random.randint = mock_random_int

    with pytest.raises(AssertionError):
        task_func()

def test_task_func_sorted_array():
    nums, pos = task_func()
    assert nums == sorted(nums), "The array should be sorted"

def test_task_func_bisect_position():
    nums, pos = task_func()
    new_num = nums[pos]
    assert all(x <= new_num for x in nums[:pos])
    assert all(x >= new_num for x in nums[pos:])