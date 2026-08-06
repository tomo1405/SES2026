import pytest
import numpy as np
import itertools
from typing import Any
from scipy import stats

def task_func(input_list: list, repetitions: int) -> Any:
    flattened_list = np.array(list(itertools.chain(*[input_list for _ in range(repetitions)])))
    mode = stats.mode(flattened_list)
    return mode