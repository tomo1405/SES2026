import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_1samp
from src_0040 import task_func


def test_task_func():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_means = np.mean(data_matrix, axis=1)
    expected_population_mean = np.mean(data_matrix)
    expected_p_value = ttest_1samp(expected_means, expected_population_mean)
    expected_significant_indices = np.where(expected_p_value < ALPHA)[0]
    expected_fig, expected_ax = plt.subplots(figsize=(10, 5))
    expected_ax.plot(expected_means, "ro", label="Means")
    expected_ax.plot(
        expected_significant_indices, expected_means[expected_significant_indices], "bo", label="Significant Means"
    )
    expected_ax.axhline(y=expected_population_mean, color="g", linestyle="-", label="Population Mean")
    expected_ax.legend()

    actual_significant_indices, actual_ax = task_func(data_matrix)

    assert np.array_equal(actual_significant_indices, expected_significant_indices)
    assert np.array_equal(actual_ax.get_lines()[0].get_xdata(), expected_means)
    assert np.array_equal(actual_ax.get_lines()[0].get_ydata(), expected_means)
    assert np.array_equal(actual_ax.get_lines()[1].get_xdata(), expected_significant_indices)
    assert np.array_equal(actual_ax.get_lines()[1].get_ydata(), expected_means[expected_significant_indices])
    assert np.array_equal(actual_ax.get_lines()[2].get_xdata(), [0, 1, 2])
    assert np.array_equal(actual_ax.get_lines()[2].get_ydata(), [expected_population_mean, expected_population_mean, expected_population_mean])
    assert actual_ax.get_legend().get_texts()[0].get_text() == "Means"
    assert actual_ax.get_legend().get_texts()[1].get_text() == "Significant Means"
    assert actual_ax.get_legend().get_texts()[2].get_text() == "Population Mean"