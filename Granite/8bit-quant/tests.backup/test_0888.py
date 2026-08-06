import pandas as pd
import numpy as np
import itertools
import pytest

from src_0888 import task_func

@pytest.mark.parametrize("T1, row_num, seed, expected_shape", [
    (
        [[1, 2, 3], [4, 5, 6]],  # T1
        100,  # row_num
        42,  # seed
        (100, 12)  # expected_shape
    ),
    (
        [[10, 20], [30, 40], [50, 60]],  # T1
        50,  # row_num
        13,  # seed
        (50, 18)  # expected_shape
    ),
])
def test_task_func(T1, row_num, seed, expected_shape):
    df = task_func(T1, row_num, seed)
    assert df.shape == expected_shape