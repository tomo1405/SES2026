python
import numpy as np
import pytest
from src_0245 import task_func

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, fft_data, ax = task_func(original)
    assert arr.size == 3
    assert fft_data.size == 3
    assert ax is not None