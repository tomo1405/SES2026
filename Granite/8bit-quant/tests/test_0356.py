import numpy as np
import pytest
from src_0356 import task_func


@pytest.mark.parametrize("amplitude, frequency, time", [
    (1.0, 1.0, np.linspace(0, 1, 100)),  # Test case 1
    (2.0, 2.0, np.linspace(0, 2, 200)),  # Test case 2
    (3.0, 3.0, np.linspace(0, 3, 300)),  # Test case 3
])
def test_task_func(amplitude, frequency, time):
    wave, fig, ax = task_func(amplitude, frequency, time)
    assert wave is not None  # Check if the wave is not None
    assert fig is not None  # Check if the figure is not None
    assert ax is not None  # Check if the axis is not None