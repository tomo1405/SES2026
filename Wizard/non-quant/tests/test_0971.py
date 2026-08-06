python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(data: np.ndarray) -> plt.Axes:
    if np.any(data < 0) or np.isnan(data).any():
        raise ValueError("Input array contains negative numbers or NaNs.")

    if not np.issubdtype(data.dtype, np.number):
        raise TypeError("Input array contains non-numeric values.")

    data_sorted = np.sort(data)
    cumulative_prob = (
        np.cumsum(data_sorted) / np.sum(data_sorted)
        if np.sum(data_sorted) != 0
        else np.zeros_like(data_sorted)
    )
    fig, ax = plt.subplots()
    ax.plot(cumulative_prob, marker="o", linestyle="-")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Probability")
    ax.set_title("Cumulative Probability Plot")

    return ax

def test_task_func():
    # Test case 1: Valid input array
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Probability"
    assert ax.get_title() == "Cumulative Probability Plot"
    assert ax.get_lines()[0].get_data()[0].tolist() == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    assert ax.get_lines()[0].get_data()[1].tolist() == [1.0, 0.8, 0.6, 0.4, 0.2, 0.0]

    # Test case 2: Input array with negative numbers
    data = np.array([1, 2, -3, 4, 5])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 3: Input array with NaNs
    data = np.array([1, 2, np.nan, 4, 5])
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 4: Input array with non-numeric values
    data = np.array([1, 2, "3", 4, 5])
    with pytest.raises(TypeError):
        task_func(data)