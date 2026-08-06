import pytest
from src_0621 import task_func
import numpy as np
import pandas as pd

@pytest.mark.parametrize("L, expected_shape", [
    ([(2, 3), (4, 5)], (8, 15)),
    ([(10, 10), (5, 5)], (50, 50)),
    ([(5, 3), (2, 2)], (10, 6)),
])
def test_task_func(L, expected_shape):
    df = task_func(L)
    assert df.shape == expected_shape