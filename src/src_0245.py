import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt
def task_func(original):
    arr = np.array([b for (_, b) in original])

    if arr.size == 0:
        fft_data = np.array([])
        return arr, fft_data, None

    fft_data = fft(arr)
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return arr, fft_data, ax