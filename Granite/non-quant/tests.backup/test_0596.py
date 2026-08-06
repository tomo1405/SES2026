import random
import bisect
from array import array
from src_0596 import task_func
import pytest

def test_task_func():
    n = 10
    total = 100
    nums, pos = task_func(n, total)
    assert isinstance(nums, array)
    assert isinstance(pos, int)
    assert len(nums) == n
    assert sum(nums) == total
    assert all(num >= 0 and num <= total for num in nums)
    new_num = random.randint(0, total)
    assert pos == bisect.bisect(nums, new_num)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1, 100)
    with pytest.raises(ValueError):
        task_func(10, -100)
    with pytest.raises(ValueError):
        task_func(10, 100, 200)