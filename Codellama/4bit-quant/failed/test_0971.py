import pytest
from src_0971 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Input array contains negative numbers or NaNs
    data = np.array([-1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        task_func(data)

    # Test 2: Input array contains non-numeric values
    data = np.array([1, 2, 3, 4, "a"])
    with pytest.raises(TypeError):
        task_func(data)

    # Test 3: Input array is empty
    data = np.array([])
    with pytest.raises(ValueError):
        task_func(data)

    # Test 4: Input array is valid
    data = np.array([1, 2, 3, 4, 5])
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Probability"
    assert ax.get_title() == "Cumulative Probability Plot"
    assert ax.get_lines()[0].get_marker() == "o"
    assert ax.get_lines()[0].get_linestyle() == "-"

if __name__ == "__main__":
    pytest.main()