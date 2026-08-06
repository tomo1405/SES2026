import random
import bisect
from array import array

def task_func(n=10, total=100):
    nums = []
    while sum(nums) != total:
        nums = [random.randint(0, total) for _ in range(n)]

    nums.sort()
    nums = array('i', nums)

    new_num = random.randint(0, total)
    pos = bisect.bisect(nums, new_num)

    return (nums, pos)

import pytest

def test_task_func():
    assert task_func(n=10, total=100)
    assert task_func(n=5, total=50)
    assert task_func(n=1, total=1)
    assert task_func(n=10, total=1000)
    assert task_func(n=100, total=10000)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(n=-1, total=100)
    with pytest.raises(ValueError):
        task_func(n=10, total=-100)
    with pytest.raises(ValueError):
        task_func(n=-1, total=-100)