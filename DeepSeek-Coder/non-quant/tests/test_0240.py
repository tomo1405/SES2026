import pytest
from src_0240 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def test_task_func():
    # Test data
    original = [(1, 2), (2, 3), (3, 4), (4, 5)]
    arr, computed_stats, _ = task_func(original)

    # Check the shape of the array
    assert arr.shape == (4,)
    
    # Check the computed statistics
    assert np.isclose(computed_stats['mean'], 3.0)
    assert np.isclose(computed_stats['std'], 1.2909944487358056)
    assert computed_stats['min'] == 2
    assert computed_stats['max'] == 4

    # Check the histogram and PDF plot
    assert plt.fignum_exists(plt.gcf().number)

    # Clean up
    plt.close('all')