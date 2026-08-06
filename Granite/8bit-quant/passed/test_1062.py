import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from pytest import mark

def task_func(arr: np.ndarray) -> (plt.Axes, np.ndarray):
    # Calculating row sums
    row_sums = arr.sum(axis=1)

    # Normalizing the data
    mean = np.mean(row_sums)
    std_dev = np.std(row_sums)
    normalized_data = (
        (row_sums - mean) / std_dev if std_dev != 0 else np.zeros_like(row_sums)
    )

    # Plotting the histogram
    _, ax = plt.subplots()
    ax.hist(normalized_data, bins=30, density=True, alpha=0.6, color="g")

    # Plotting the PDF of a standard normal distribution
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
    ax.plot(x, norm.pdf(x), "r-", lw=2)
    ax.set_title("Histogram of Normalized Data with Standard Normal PDF")

    return ax, normalized_data

@mark.parametrize("arr", [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])])
def test_task_func(arr):
    ax, normalized_data = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert isinstance(normalized_data, np.ndarray)
    assert normalized_data.shape == arr.shape