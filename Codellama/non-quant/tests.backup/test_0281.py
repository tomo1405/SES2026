import pytest
from src_0281 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def test_task_func():
    signal = np.array([1, 2, 3, 4, 5])
    precision = 2
    seed = 777
    np.random.seed(seed)
    transformed_signal = fft(signal)
    transformed_signal_rounded = np.round(transformed_signal, precision).tolist()

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(signal)
    ax[0].set_title('Original Signal')
    ax[1].plot(transformed_signal_rounded)
    ax[1].set_title('Transformed Signal')
    plt.tight_layout()  # Adjust layout to avoid overlap

    assert np.array_equal(task_func(signal, precision, seed), np.array(transformed_signal_rounded))
    assert ax[0].get_title() == 'Original Signal'
    assert ax[1].get_title() == 'Transformed Signal'
    plt.close()