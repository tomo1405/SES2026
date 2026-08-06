python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2*np.pi, 0.01)

def task_func(n_waves, seed=0):
    np.random.seed(seed)
    sine_wave_series = []

    if n_waves < 1:
        return sine_wave_series, np.array([]), None

    for frequency in range(1, n_waves+1):
        wave = np.sin(frequency * ANGLES)
        sine_wave_series.append(wave)

    fft_data = fft(np.sum(sine_wave_series, axis=0))
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return sine_wave_series, fft_data, ax

def test_task_func():
    sine_wave_series, fft_data, ax = task_func(3, seed=42)
    assert len(sine_wave_series) == 3
    assert sine_wave_series[0].shape == (100,)
    assert sine_wave_series[1].shape == (100,)
    assert sine_wave_series[2].shape == (100,)
    assert fft_data.shape == (100,)
    assert ax is not None

test_task_func()