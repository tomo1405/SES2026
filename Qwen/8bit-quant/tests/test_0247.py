import numpy as np
from src_0247 import task_func


def test_task_func_no_waves():
    sine_wave_series, fft_data, ax = task_func(0)
    assert sine_wave_series == []
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size == 0
    assert ax is None

def test_task_func_one_wave():
    sine_wave_series, fft_data, ax = task_func(1)
    assert len(sine_wave_series) == 1
    assert isinstance(sine_wave_series[0], np.ndarray)
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size > 0
    assert ax is not None

def test_task_func_multiple_waves():
    sine_wave_series, fft_data, ax = task_func(5)
    assert len(sine_wave_series) == 5
    for wave in sine_wave_series:
        assert isinstance(wave, np.ndarray)
    assert isinstance(fft_data, np.ndarray)
    assert fft_data.size > 0
    assert ax is not None

def test_task_func_seed_consistency():
    sine_wave_series_1, fft_data_1, _ = task_func(3, seed=42)
    sine_wave_series_2, fft_data_2, _ = task_func(3, seed=42)
    assert np.array_equal(sine_wave_series_1, sine_wave_series_2)
    assert np.array_equal(fft_data_1, fft_data_2)

def test_task_func_fft_data_length():
    sine_wave_series, fft_data, _ = task_func(10)
    assert len(fft_data) == len(ANGLES)