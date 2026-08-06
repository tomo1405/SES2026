import pytest
from src_0281 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

@pytest.fixture
def setup():
    np.random.seed(777)
    signal = np.random.rand(10)
    return signal

def test_task_func(setup):
    signal = setup
    result, _ = task_func(signal)
    assert isinstance(result, np.ndarray), "The result should be a numpy array"
    assert len(result) == len(signal), "The length of the result should be the same as the input signal"

def test_plot(setup):
    signal = setup
    _, ax = task_func(signal)
    assert len(ax) == 2, "Expected 2 subplots"
    assert ax[0].get_title() == 'Original Signal', "The first plot should be the original signal"
    assert ax[1].get_title() == 'Transformed Signal', "The second plot should be the transformed signal"