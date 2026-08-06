import pytest
from src_0268 import task_func

def test_task_func():
    data = {'a': 1, 'b': 2, 'c': 3}
    sample_rate = 8000
    fft, ax = task_func(data, sample_rate)
    assert fft is not None
    assert ax is not None
    assert ax.get_title() == 'FFT of the Signal'
    assert ax.get_xlabel() == 'Frequency [Hz]'
    assert ax.get_ylabel() == 'Frequency Spectrum Magnitude'