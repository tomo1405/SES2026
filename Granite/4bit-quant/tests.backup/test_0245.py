import pytest
from src_0245 import task_func

def test_task_func():
    original = [("a", 1), ("b", 2), ("c", 3)]
    arr, fft_data, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert isinstance(fft_data, np.ndarray)
    assert ax is not None
    assert len(arr) == len(original)
    assert len(fft_data) == len(arr)