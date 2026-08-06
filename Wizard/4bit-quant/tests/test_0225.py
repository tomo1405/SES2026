python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def task_func(range_start=-10, range_end=10, step=0.1):
    if range_start>range_end:
        raise ValueError("range_start cannot be smaller than range_end.")

    x_values = np.arange(range_start, range_end, step)
    data = ((x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x))) for x in x_values)
    fft_values = fft([abs(np.sin(x) - np.cos(x)) for x in x_values])
    _, ax = plt.subplots()
    for x, sin_x, cos_x, abs_x in data:
        ax.scatter(x, sin_x, color='b')
        ax.scatter(x, cos_x, color='r')
        ax.scatter(x, abs_x, color='g')
    
    # We recreate the generator since it was exhausted in the for loop above
    data = ((x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x))) for x in x_values)
    return data, ax, abs(np.mean(fft_values)), abs(np.median(fft_values))

def test_task_func():
    data, ax, mean_fft, median_fft = task_func()
    assert len(data) == 101
    assert len(ax.collections) == 303
    assert abs(mean_fft - 0.0001461791442825175) < 1e-6
    assert abs(median_fft - 0.0001461791442825175) < 1e-6