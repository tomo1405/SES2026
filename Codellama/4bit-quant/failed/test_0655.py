import pytest
from src_0655 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    # Test with valid input
    array = np.array([[1, 2], [3, 4], [5, 6]])
    target_value = 2
    popt, ax = task_func(array, target_value)
    assert np.allclose(popt, [1, 0.1, 2])
    assert ax.get_title() == "Fitting Function"
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_legend() == "Data"
    assert ax.get_legend() == "Fit"

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4], [5, 6]]), 10)

if __name__ == "__main__":
    pytest.main()