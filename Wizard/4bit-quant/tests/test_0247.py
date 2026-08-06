python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from src_0247 import task_func

def test_task_func():
    ANGLES = np.arange(0, 2*np.pi, 0.01)
    sine_wave_series, fft_data, ax = task_func(3, seed=0)
    assert len(sine_wave_series) == 3
    assert sine_wave_series[0].shape == (100,)
    assert fft_data.shape == (100,)
    assert ax is not None