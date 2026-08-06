import pytest
from src_0655 import task_func
import numpy as np

def test_task_func():
    # Test with valid input
    array = np.array([[1, 2], [3, 4], [5, 6]])
    target_value = 3
    popt, ax = task_func(array, target_value)
    assert np.allclose(popt, [1, 0.1, 4])
    assert ax.get_title() == "Fitting Function"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_label() == "Data"
    assert ax.get_lines()[1].get_label() == "Fit"

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(array, 10)