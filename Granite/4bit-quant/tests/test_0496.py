import pandas as pd
import numpy as np
import pytest

from src_0496 import task_func

@pytest.mark.parametrize("days,random_seed,expected_shape", [
    (10, 0, (10, 6)),
    (5, 1, (5, 6)),
    (15, 2, (15, 6)),
])
def test_task_func(days, random_seed, expected_shape):
    df = task_func(days, random_seed)
    assert df.shape == expected_shape, "Generated dataframe has incorrect shape"

def test_task_func_default_args():
    df = task_func()
    assert df.shape == (10, 6), "Generated dataframe has incorrect shape"

def test_task_func_invalid_args():
    with pytest.raises(ValueError):
        task_func("foo", "bar")