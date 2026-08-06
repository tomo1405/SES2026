import pytest
from src_0247 import task_func

def test_task_func():
    # Test case 1: n_waves = 1
    sine_wave_series, fft_data, ax = task_func(n_waves=1)
    assert len(sine_wave_series) == 1
    assert len(fft_data) == 1
    assert ax.get_title() == "Sine Wave Series"

    # Test case 2: n_waves = 2
    sine_wave_series, fft_data, ax = task_func(n_waves=2)
    assert len(sine_wave_series) == 2
    assert len(fft_data) == 2
    assert ax.get_title() == "Sine Wave Series"

    # Test case 3: n_waves = 3
    sine_wave_series, fft_data, ax = task_func(n_waves=3)
    assert len(sine_wave_series) == 3
    assert len(fft_data) == 3
    assert ax.get_title() == "Sine Wave Series"

    # Test case 4: n_waves = 4
    sine_wave_series, fft_data, ax = task_func(n_waves=4)
    assert len(sine_wave_series) == 4
    assert len(fft_data) == 4
    assert ax.get_title() == "Sine Wave Series"

    # Test case 5: n_waves = 5
    sine_wave_series, fft_data, ax = task_func(n_waves=5)
    assert len(sine_wave_series) == 5
    assert len(fft_data) == 5
    assert ax.get_title() == "Sine Wave Series"

    # Test case 6: n_waves = 6
    sine_wave_series, fft_data, ax = task_func(n_waves=6)
    assert len(sine_wave_series) == 6
    assert len(fft_data) == 6
    assert ax.get_title() == "Sine Wave Series"

    # Test case 7: n_waves = 7
    sine_wave_series, fft_data, ax = task_func(n_waves=7)
    assert len(sine_wave_series) == 7
    assert len(fft_data) == 7
    assert ax.get_title() == "Sine Wave Series"

    # Test case 8: n_waves = 8
    sine_wave_series, fft_data, ax = task_func(n_waves=8)
    assert len(sine_wave_series) == 8
    assert len(fft_data) == 8
    assert ax.get_title() == "Sine Wave Series"

    # Test case 9: n_waves = 9
    sine_wave_series, fft_data, ax = task_func(n_waves=9)
    assert len(sine_wave_series) == 9
    assert len(fft_data) == 9
    assert ax.get_title() == "Sine Wave Series"

    # Test case 10: n_waves = 10
    sine_wave_series, fft_data, ax = task_func(n_waves=10)
    assert len(sine_wave_series) == 10
    assert len(fft_data) == 10
    assert ax.get_title() == "Sine Wave Series"