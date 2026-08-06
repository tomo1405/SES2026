import pytest
from src_0596 import task_func

def test_task_func():
    nums, pos = task_func()
    assert len(nums) == 10
    assert sum(nums) == 100
    assert pos >= 0 and pos <= len(nums)

def test_task_func_with_n():
    nums, pos = task_func(n=5)
    assert len(nums) == 5
    assert sum(nums) == 100
    assert pos >= 0 and pos <= len(nums)

def test_task_func_with_total():
    nums, pos = task_func(total=50)
    assert len(nums) == 10
    assert sum(nums) == 50
    assert pos >= 0 and pos <= len(nums)

def test_task_func_with_n_and_total():
    nums, pos = task_func(n=5, total=50)
    assert len(nums) == 5
    assert sum(nums) == 50
    assert pos >= 0 and pos <= len(nums)