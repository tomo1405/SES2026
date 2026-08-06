import numpy as np
from src_1066 import task_func


def test_task_func():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax = task_func(arr)
    assert ax.get_title() == "Absolute values of FFT coefficients"
    assert np.allclose(ax.get_xdata(), np.abs(fftpack.fft(arr.sum(axis=1))))
    assert np.allclose(ax.get_ydata(), np.abs(fftpack.fft(arr.sum(axis=1))))