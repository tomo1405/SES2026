import pytest
from src_0281 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple signal
    signal = np.array([0, 1, 2, 3])
    expected_transformed_signal = np.array([6, -2+2j, -2, -2-2j])

    transformed_signal, ax = task_func(signal)

    # Check if the transformed signal is as expected
    assert np.allclose(transformed_signal, expected_transformed_signal, atol=1e-2)

    # Check if the plot has two subplots
    assert len(ax) == 2

    # Check if the first subplot title is correct
    assert ax[0].get_title() == 'Original Signal'

    # Check if the second subplot title is correct
    assert ax[1].get_title() == 'Transformed Signal'

    # Close the plot to prevent it from displaying
    plt.close(fig)