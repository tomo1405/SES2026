import numpy as np
import itertools
import random
from src_0012 import task_func

def test_task_func():
    T1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    p25, p50, p75 = task_func(T1)
    assert isinstance(p25, float) and isinstance(p50, float) and isinstance(p75, float)
    assert 0 <= p25 <= 100 and 0 <= p50 <= 100 and 0 <= p75 <= 100
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)
    random_nums = [random.randint(0, 100) for _ in range(total_nums)]
    assert np.percentile(random_nums, 25) == p25
    assert np.percentile(random_nums, 50) == p50
    assert np.percentile(random_nums, 75) == p75