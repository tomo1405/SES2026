import pytest
from src_0062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def test_task_func():
    # Test case 1: Test that the function returns the correct square roots
    result = [{'from_user': 1}, {'from_user': 4}, {'from_user': 9}]
    expected_square_roots = np.round(np.sqrt([1, 4, 9]), 2)
    square_roots, ax = task_func(result)
    assert np.array_equal(square_roots, expected_square_roots)

    # Test case 2: Test that the function plots the correct data
    result = [{'from_user': 1}, {'from_user': 4}, {'from_user': 9}]
    expected_x_values = [1, 4, 9]
    expected_y_values = np.round(np.sqrt([1, 4, 9]), 2)
    square_roots, ax = task_func(result)
    assert np.array_equal(ax.get_xdata(), expected_x_values)
    assert np.array_equal(ax.get_ydata(), expected_y_values)

    # Test case 3: Test that the function annotates the plot with the correct date and time
    result = [{'from_user': 1}, {'from_user': 4}, {'from_user': 9}]
    expected_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    square_roots, ax = task_func(result)
    assert ax.get_title() == 'Square root plot'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'sqrt(x)'
    assert ax.get_annotations()[0].get_text() == expected_date_time