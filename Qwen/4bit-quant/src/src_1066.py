from scipy import fftpack
from matplotlib import pyplot as plt
def task_func(arr):
    row_sums = arr.sum(axis=1)
    fft_coefficients = fftpack.fft(row_sums)

    _, ax = plt.subplots()
    ax.plot(np.abs(fft_coefficients))
    ax.set_title("Absolute values of FFT coefficients")

    return ax