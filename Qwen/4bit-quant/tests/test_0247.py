import numpy as np
from src_0247 import task_func


def test_task_func_no_waves():
    sine_wave_series, fft_data, ax = task_func(0)
    assert sine_wave_series == []
    assert np.array_equal(fft_data, np.array([]))
    assert ax is None

def test_task_func_one_wave():
    sine_wave_series, fft_data, ax = task_func(1)
    assert len(sine_wave_series) == 1
    assert np.allclose(sine_wave_series[0], np.sin(ANGLES))
    assert isinstance(fft_data, np.ndarray)
    assert ax is not None

def test_task_func_multiple_waves():
    sine_wave_series, fft_data, ax = task_func(3)
    assert len(sine_wave_series) == 3
    assert np.allclose(sine_wave_series[0], np.sin(ANGLES))
    assert np.allclose(sine_wave_series[1], np.sin(2 * ANGLES))
    assert np.allclose(sine_wave_series[2], np.sin(3 * ANGLES))
    assert isinstance(fft_data, np.ndarray)
    assert ax is not None

def test_task_func_with_seed():
    sine_wave_series_1, fft_data_1, _ = task_func(2, seed=42)
    sine_wave_series_2, fft_data_2, _ = task_func(2, seed=42)
    assert np.array_equal(sine_wave_series_1, sine_wave_series_2)
    assert np.array_equal(fft_data_1, fft_data_2)

def test_task_func_fft_data_length():
    sine_wave_series, fft_data, _ = task_func(5)
    assert len(fft_data) == len(ANGLES)

def test_task_func_fft_data_type():
    sine_wave_series, fft_data, _ = task_func(1)
    assert isinstance(fft_data, np.ndarray)