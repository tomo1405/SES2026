import pytest
from src_0596 import task_func

def test_task_func():
    n = 10
    total = 100
    nums, pos = task_func(n, total)
    assert isinstance(nums, list)
    assert isinstance(pos, int)
    assert len(nums) == n
    assert sum(nums) == total
    assert all(num >= 0 and num <= total for num in nums)
    assert pos >= 0 and pos <= n
    assert nums[pos-1] <= new_num <= nums[pos] if pos > 0 else nums[pos] == new_num