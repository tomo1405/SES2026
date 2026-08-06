import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
ANGLES = np.arange(0, 2*np.pi, 0.01)
from src_0247 import task_func

def test_task_func_with_n_waves_less_than_1():
    n_waves = 0
    sine_wave_series, fft_data, ax = task_func(n_waves)
    assert sine_wave_series == []
    assert fft_data is None
    assert ax is None

def test_task_func_with_n_waves_1():
    n_waves = 1
    sine_wave_series, fft_data, ax = task_func(n_waves)
    assert len(sine_wave_series) == 1
    assert fft_data.shape == (ANGLES.shape[0],)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_n_waves_2():
    n_waves = 2
    sine_wave_series, fft_data, ax = task_func(n_waves)
    assert len(sine_wave_series) == 2
    assert fft_data.shape == (ANGLES.shape[0],)
    assert isinstance(ax, plt.Axes)