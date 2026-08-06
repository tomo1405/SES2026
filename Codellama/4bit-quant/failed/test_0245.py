import pytest
from src_0245 import task_func
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, fft_data, ax = task_func(original)
    assert arr.size == 3
    assert fft_data.size == 3
    assert ax is not None
    assert ax.get_title() == "Histogram of FFT Data"
    assert ax.get_xlabel() == "Frequency"
    assert ax.get_ylabel() == "Amplitude"
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 10)

def test_task_func_empty():
    original = []
    arr, fft_data, ax = task_func(original)
    assert arr.size == 0
    assert fft_data.size == 0
    assert ax is None

def test_task_func_invalid():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, fft_data, ax = task_func(original)
    assert arr.size == 3
    assert fft_data.size == 3
    assert ax is not None
    assert ax.get_title() == "Histogram of FFT Data"
    assert ax.get_xlabel() == "Frequency"
    assert ax.get_ylabel() == "Amplitude"
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 10)

if __name__ == "__main__":
    pytest.main()