import numpy as np
import random
from scipy import stats
from src_0312 import task_func

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
    random.seed(0)
    expected_result = {
        'mean': np.mean([1, 2, 3, 4, 5, 6, 7, 8, 9]),
        'median': np.median([1, 2, 3, 4, 5, 6, 7, 8, 9]),
        'mode': stats.mode([1, 2, 3, 4, 5, 6, 7, 8, 9])[0][0]
    }
    result = task_func(list_of_lists)
    assert result == expected_result

def test_task_func_with_seed_and_size():
    list_of_lists = [[1, 2, 3], [], [4, 5, 6], [7, 8, 9]]
    seed = 0
    size = 10
    random.seed(seed)
    expected_result = {
        'mean': np.mean([1, 2, 3, 4, 5, 6, 7, 8, 9] + [random.randint(0, 100) for _ in range(size)]),
        'median': np.median([1, 2, 3, 4, 5, 6, 7, 8, 9] + [random.randint(0, 100) for _ in range(size)]),
        'mode': stats.mode([1, 2, 3, 4, 5, 6, 7, 8, 9] + [random.randint(0, 100) for _ in range(size)])[0][0]
    }
    result = task_func(list_of_lists, size=size, seed=seed)
    assert result == expected_result