python
import numpy as np
import pytest
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

# Constants
ALPHA = 0.05

def task_func(data_matrix):
    means = np.mean(data_matrix, axis=1)
    population_mean = np.mean(data_matrix)

    _, p_value = ttest_1samp(means, population_mean)
    significant_indices = np.where(p_value < ALPHA)[0]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(means, "ro", label="Means")
    ax.plot(
        significant_indices, means[significant_indices], "bo", label="Significant Means"
    )
    ax.axhline(y=population_mean, color="g", linestyle="-", label="Population Mean")
    ax.legend()
    return significant_indices.tolist(), ax

def test_task_func():
    # Test case 1
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    significant_indices, ax = task_func(data_matrix)
    assert significant_indices == [0, 1, 2]
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Mean"
    assert ax.get_title() == "Means and Significant Means"
    assert ax.get_xticks() == [0, 1, 2]
    assert ax.get_xticklabels() == ["0", "1", "2"]
    assert ax.get_yticks() == [2.5, 5.5, 8.5]
    assert ax.get_yticklabels() == ["2.5", "5.5", "8.5"]
    assert ax.get_legend_handles_labels() == (
        [
            plt.Line2D([0], [0], color="r", lw=2, label="Means"),
            plt.Line2D([0], [0], color="b", lw=2, label="Significant Means"),
            plt.Line2D([0], [0], color="g", lw=2, label="Population Mean"),
        ],
        ["Means", "Significant Means", "Population Mean"],
    )

    # Test case 2
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    significant_indices, ax = task_func(data_matrix)
    assert significant_indices == [0, 1, 2, 3]
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Mean"
    assert ax.get_title() == "Means and Significant Means"
    assert ax.get_xticks() == [0, 1, 2, 3]
    assert ax.get_xticklabels() == ["0", "1", "2", "3"]
    assert ax.get_yticks() == [2.5, 5.5, 8.5, 11.5]
    assert ax.get_yticklabels() == ["2.5", "5.5", "8.5", "11.5"]
    assert ax.get_legend_handles_labels() == (
        [
            plt.Line2D([0], [0], color="r", lw=2, label="Means"),
            plt.Line2D([0], [0], color="b", lw=2, label="Significant Means"),
            plt.Line2D([0], [0], color="g", lw=2, label="Population Mean"),
        ],
        ["Means", "Significant Means", "Population Mean"],
    )

    # Test case 3
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
    significant_indices, ax = task_func(data_matrix)
    assert significant_indices == [0, 1, 2, 3, 4]
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Mean"
    assert ax.get_title() == "Means and Significant Means"
    assert ax.get_xticks() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels() == ["0", "1", "2", "3", "4"]
    assert ax.get_yticks() == [2.5, 5.5, 8.5, 11.5, 14.5]
    assert ax.get_yticklabels() == ["2.5", "5.5", "8.5", "11.5", "14.5"]
    assert ax.get_legend_handles_labels() == (
        [
            plt.Line2D([0], [0], color="r", lw=2, label="Means"),
            plt.Line2D([0], [0], color="b", lw=2, label="Significant Means"),
            plt.Line2D([0], [0], color="g", lw=2, label="Population Mean"),
        ],
        ["Means", "Significant Means", "Population Mean"],
    )