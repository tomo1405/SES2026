import pytest
from src_0059 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def mock_plt(mocker):
    mocker.patch('matplotlib.pyplot.subplots', return_value=(plt.figure(), plt.gca()))
    mocker.patch('matplotlib.pyplot.xlim', return_value=(-3, 3))
    mocker.patch('matplotlib.pyplot.show')

def test_task_func(mock_plt):
    mu = 0
    sigma = 1
    num_samples = 1000
    fig = task_func(mu, sigma, num_samples)
    
    assert isinstance(fig, plt.Figure)
    mock_plt.subplots.assert_called_once()
    mock_plt.xlim.assert_called_once()
    mock_plt.show.assert_called_once()

    # Additional checks can be added to verify the histogram and plot properties
    # However, since we are not modifying the target code, we will not do so here.