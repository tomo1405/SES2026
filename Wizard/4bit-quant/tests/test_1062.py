python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pytest

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

def test_task_func():
    # Test case 1
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    ax, normalized_data = task_func(arr)
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"
    assert np.allclose(normalized_data, np.array([[-1.34164079, -0.4472136 ],
                                                 [ 0.4472136 ,  1.34164079]]))

    # Test case 2
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax, normalized_data = task_func(arr)
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"
    assert np.allclose(normalized_data, np.array([[-1.34164079, -0.4472136 ],
                                                 [ 0.4472136 ,  1.34164079],
                                                 [ 2.23606798,  3.16227766]]))

    # Test case 3
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    ax, normalized_data = task_func(arr)
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"
    assert np.allclose(normalized_data, np.array([[-1.34164079, -0.4472136 ],
                                                 [ 0.4472136 ,  1.34164079],
                                                 [ 2.23606798,  3.16227766],
                                                 [ 4.12310563,  5.09901951]]))

    # Test case 4
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
    ax, normalized_data = task_func(arr)
    assert ax.get_title() == "Histogram of Normalized Data with Standard Normal PDF"
    assert np.allclose(normalized_data, np.array([[-1.34164079, -0.4472136 ],
                                                 [ 0.4472136 ,  1.34164079],
                                                 [ 2.23606798,  3.16227766],
                                                 [ 4.12310563,  5.09901951],
                                                 [ 6.00000000,  6.92820323]]))