import pytest
from src_0247 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def test_task_func_zero_waves():
    sine_wave_series, fft_data, ax = task_func(0)
    assert sine_wave_series == []
    assert np.array_equal(fft_data, np.array([]))
    assert ax is None

def test_task_func_one_wave():
    sine_wave_series, fft_data, ax = task_func(1)
    assert len(sine_wave_series) == 1
    assert np.allclose(sine_wave_series[0], np.sin(ANGLES))
    assert fft_data.size > 0
    assert isinstance(ax, plt.Axes)

def test_task_func_multiple_waves():
    sine_wave_series, fft_data, ax = task_func(3)
    assert len(sine_wave_series) == 3
    assert np.allclose(sine_wave_series[0], np.sin(ANGLES))
    assert np.allclose(sine_wave_series[1], np.sin(2 * ANGLES))
    assert np.allclose(sine_wave_series[2], np.sin(3 * ANGLES))
    assert fft_data.size > 0
    assert isinstance(ax, plt.Axes)

def test_task_func_seed_consistency():
    sine_wave_series_1, _, _ = task_func(2, seed=42)
    sine_wave_series_2, _, _ = task_func(2, seed=42)
    assert np.array_equal(sine_wave_series_1, sine_wave_series_2)

def test_task_func_fft_data():
    sine_wave_series, fft_data, _ = task_func(2)
    expected_fft_data = fft(np.sin(ANGLES) + np.sin(2 * ANGLES))
    assert np.allclose(fft_data, expected_fft_data)