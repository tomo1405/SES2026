python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pytest

def task_func(mu, sigma, num_samples):
    samples = np.random.normal(mu, sigma, num_samples)
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2)

    ax.set_title('Normal Distribution')
    plt.show()
    return fig

def test_task_func():
    # Test case 1
    mu = 0
    sigma = 1
    num_samples = 1000
    fig = task_func(mu, sigma, num_samples)
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == 'Normal Distribution'
    assert len(fig.axes[0].patches) == 30
    assert fig.axes[0].patches[0].get_height() == pytest.approx(0.002, 0.01)
    assert fig.axes[0].patches[-1].get_height() == pytest.approx(0.002, 0.01)
    assert fig.axes[0].patches[0].get_x() == pytest.approx(-2.5, 0.1)
    assert fig.axes[0].patches[-1].get_x() == pytest.approx(2.5, 0.1)
    assert fig.axes[0].patches[0].get_facecolor() == (0.0, 0.6666666666666666, 0.0, 1.0)
    assert fig.axes[0].patches[-1].get_facecolor() == (0.0, 0.6666666666666666, 0.0, 1.0)
    assert fig.axes[0].lines[0].get_color() == (0.0, 0.0, 0.0, 1.0)
    assert fig.axes[0].lines[0].get_linewidth() == 2.0
    assert fig.axes[0].lines[0].get_data()[0][0] == pytest.approx(-2.5, 0.1)
    assert fig.axes[0].lines[0].get_data()[0][-1] == pytest.approx(2.5, 0.1)
    assert fig.axes[0].lines[0].get_data()[1][0] == pytest.approx(0.0, 0.01)
    assert fig.axes[0].lines[0].get_data()[1][-1] == pytest.approx(0.0, 0.01)

    # Test case 2
    mu = 1
    sigma = 2
    num_samples = 500
    fig = task_func(mu, sigma, num_samples)
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == 'Normal Distribution'
    assert len(fig.axes[0].patches) == 30
    assert fig.axes[0].patches[0].get_height() == pytest.approx(0.0007, 0.001)
    assert fig.axes[0].patches[-1].get_height() == pytest.approx(0.0007, 0.001)
    assert fig.axes[0].patches[0].get_x() == pytest.approx(-5.0, 0.1)
    assert fig.axes[0].patches[-1].get_x() == pytest.approx(5.0, 0.1)
    assert fig.axes[0].patches[0].get_facecolor() == (0.0, 0.6666666666666666, 0.0, 1.0)
    assert fig.axes[0].patches[-1].get_facecolor() == (0.0, 0.6666666666666666, 0.0, 1.0)
    assert fig.axes[0].lines[0].get_color() == (0.0, 0.0, 0.0, 1.0)
    assert fig.axes[0].lines[0].get_linewidth() == 2.0
    assert fig.axes[0].lines[0].get_data()[0][0] == pytest.approx(-5.0, 0.1)
    assert fig.axes[0].lines[0].get_data()[0][-1] == pytest.approx(5.0, 0.1)
    assert fig.axes[0].lines[0].get_data()[1][0] == pytest.approx(0.0, 0.001)
    assert fig.axes[0].lines[0].get_data()[1][-1] == pytest.approx(0.0, 0.001)