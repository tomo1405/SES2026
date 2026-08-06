import numpy as np
from src_0247 import task_func


def test_task_func_n_waves_less_than_1():
    sine_wave_series, fft_data, ax = task_func(n_waves=0)
    assert sine_wave_series == []
    assert fft_data == np.array([])
    assert ax is None

def test_task_func_n_waves_greater_than_1():
    sine_wave_series, fft_data, ax = task_func(n_waves=2)
    assert len(sine_wave_series) == 2
    assert len(fft_data) == 2
    assert ax is not None
    assert isinstance(ax, plt.Axes)