import pytest
from src_0240 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test case 1: Test that the function returns the correct values
    original = [(1, 2), (3, 4), (5, 6), (7, 8)]
    arr, computed_stats, ax = task_func(original)
    assert np.allclose(arr, np.array([2, 4, 6, 8]))
    assert computed_stats['mean'] == 5
    assert computed_stats['std'] == 2
    assert computed_stats['min'] == 2
    assert computed_stats['max'] == 8

    # Test case 2: Test that the function plots the histogram and PDF correctly
    fig, ax = plt.subplots()
    ax.hist(arr, density=True, alpha=0.6, bins='auto', label='Histogram')
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, computed_stats['mean'], computed_stats['std'])
    ax.plot(x, p, 'k', linewidth=2, label='PDF')
    ax.set_title('Histogram with PDF')
    ax.legend()
    plt.close(fig)

    # Test case 3: Test that the function raises an error when the input is not a list of tuples
    with pytest.raises(TypeError):
        task_func(1)

    # Test case 4: Test that the function raises an error when the input list is empty
    with pytest.raises(ValueError):
        task_func([])