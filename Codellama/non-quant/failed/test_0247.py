import pytest
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

def test_task_func_seed_0():
    sine_wave_series, fft_data, ax = task_func(n_waves=2, seed=0)
    assert sine_wave_series[0] == np.sin(1 * ANGLES)
    assert sine_wave_series[1] == np.sin(2 * ANGLES)
    assert fft_data[0] == fft(np.sin(1 * ANGLES) + np.sin(2 * ANGLES))
    assert fft_data[1] == fft(np.sin(2 * ANGLES) + np.sin(3 * ANGLES))
    assert ax.hist(np.abs(fft_data)) == [0, 1, 2, 3, 4]

def test_task_func_seed_1():
    sine_wave_series, fft_data, ax = task_func(n_waves=2, seed=1)
    assert sine_wave_series[0] == np.sin(1 * ANGLES)
    assert sine_wave_series[1] == np.sin(2 * ANGLES)
    assert fft_data[0] == fft(np.sin(1 * ANGLES) + np.sin(2 * ANGLES))
    assert fft_data[1] == fft(np.sin(2 * ANGLES) + np.sin(3 * ANGLES))
    assert ax.hist(np.abs(fft_data)) == [0, 1, 2, 3, 4]