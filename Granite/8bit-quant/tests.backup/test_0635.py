import pytest
from src_0635 import task_func
import numpy as np
import itertools
from scipy import stats

def test_task_func():
    input_list = [1, 2, 3, 4, 5]
    repetitions = 3
    expected_result = stats.mode(np.array(list(itertools.chain(*[input_list for _ in range(repetitions)]))))
    
    actual_result = task_func(input_list, repetitions)
    
    assert actual_result.mode[0] == expected_result.mode[0]
    assert actual_result.count[0] == expected_result.count[0]