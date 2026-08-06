import pytest
from src_0596 import task_func

def test_task_func():
    n = 10
    total = 100
    nums, pos = task_func(n, total)
    assert len(nums) == n
    assert sum(nums) == total
    assert pos >= 0 and pos <= n
    assert nums[pos] >= new_num