import numpy as np
import pytest
from src_0356 import task_func


@pytest.mark.parametrize("amplitude, frequency, time", [
    (1.0, 1.0, np.linspace(0, 1, 100)),
    (2.0, 2.0, np.linspace(0, 2, 200)),
    (3.0, 3.0, np.linspace(0, 3, 300)),
])
def test_task_func(amplitude, frequency, time):
    wave, fig, ax = task_func(amplitude, frequency, time)
    assert wave.shape == time.shape
    assert fig is not None
    assert ax is not None