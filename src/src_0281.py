import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
def task_func(signal, precision=2, seed=777):
    np.random.seed(seed)
    transformed_signal = fft(signal)
    transformed_signal_rounded = np.round(transformed_signal, precision).tolist()

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(signal)
    ax[0].set_title('Original Signal')
    ax[1].plot(transformed_signal_rounded)
    ax[1].set_title('Transformed Signal')
    plt.tight_layout()  # Adjust layout to avoid overlap

    return np.array(transformed_signal_rounded), ax