import pytest
from src_0059 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def mock_plt(mocker):
    return mocker.patch('src_0059.plt')

def test_task_func(mock_plt):
    mu = 0
    sigma = 1
    num_samples = 1000
    fig = task_func(mu, sigma, num_samples)

    # Check that plt.subplots was called
    mock_plt.subplots.assert_called_once()

    # Check that plt.hist was called with the correct parameters
    mock_plt.hist.assert_called_once_with(
        mocker.ANY, bins=30, density=True, alpha=0.6, color='g'
    )

    # Check that plt.xlim was called
    mock_plt.xlim.assert_called_once()

    # Check that plt.plot was called with the correct parameters
    mock_plt.plot.assert_called_once()

    # Check that plt.title was called with the correct title
    mock_plt.title.assert_called_once_with('Normal Distribution')

    # Check that plt.show was called
    mock_plt.show.assert_called_once()

    # Check that the returned figure is a matplotlib Figure object
    assert isinstance(fig, plt.Figure)