import pytest
from src_0225 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def test_task_func():
    # Test case 1: range_start < range_end
    range_start = -10
    range_end = 10
    step = 0.1
    data, ax, mean_fft, median_fft = task_func(range_start, range_end, step)
    assert data is not None
    assert ax is not None
    assert mean_fft is not None
    assert median_fft is not None

    # Test case 2: range_start > range_end
    range_start = 10
    range_end = -10
    step = 0.1
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)

    # Test case 3: step = 0
    range_start = -10
    range_end = 10
    step = 0
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)

    # Test case 4: range_start = range_end
    range_start = 10
    range_end = 10
    step = 0.1
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)

    # Test case 5: range_start = range_end = 0
    range_start = 0
    range_end = 0
    step = 0.1
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)

    # Test case 6: range_start = range_end = 0, step = 0
    range_start = 0
    range_end = 0
    step = 0
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)

    # Test case 7: range_start = range_end = 0, step = 0.1
    range_start = 0
    range_end = 0
    step = 0.1
    data, ax, mean_fft, median_fft = task_func(range_start, range_end, step)
    assert data is not None
    assert ax is not None
    assert mean_fft is not None
    assert median_fft is not None

    # Test case 8: range_start = range_end = 0, step = 0.1, range_start < range_end
    range_start = 0
    range_end = 0
    step = 0.1
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)

    # Test case 9: range_start = range_end = 0, step = 0.1, range_start > range_end
    range_start = 0
    range_end = 0
    step = 0.1
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)

    # Test case 10: range_start = range_end = 0, step = 0.1, range_start = range_end
    range_start = 0
    range_end = 0
    step = 0.1
    with pytest.raises(ValueError):
        task_func(range_start, range_end, step)