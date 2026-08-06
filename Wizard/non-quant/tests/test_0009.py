python
import pytest
from src_0009 import task_func

def test_task_func():
    T1 = ["1 2 3", "4 5 6"]
    RANGE = 100
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)

    random_nums = [randint(0, RANGE) for _ in range(total_nums)]
    counts = Counter(random_nums)

    assert task_func(T1, RANGE) == counts