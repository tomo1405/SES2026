python
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pytest

def task_func(mean, std_dev, num_samples):
    samples = np.random.normal(mean, std_dev, num_samples)
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mean = %.2f,  std = %.2f" % (mean, std_dev)
    ax.set_title(title)

    return samples, fig

def test_task_func():
    # Test case 1: mean = 0, std_dev = 1, num_samples = 1000
    mean = 0
    std_dev = 1
    num_samples = 1000
    samples, fig = task_func(mean, std_dev, num_samples)
    assert samples.shape == (num_samples,)
    assert fig is not None
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == "Fit results: mean = 0.00,  std = 1.00"
    assert fig.axes[0].get_xlabel() == "Values"
    assert fig.axes[0].get_ylabel() == "Density"
    assert fig.axes[0].get_xlim() == (-3.5, 3.5)
    assert fig.axes[0].get_ylim() == (0, 0.45)
    assert fig.axes[0].get_xticks() == [-3, -2, -1, 0, 1, 2, 3]
    assert fig.axes[0].get_yticks() == [0, 0.1, 0.2, 0.3, 0.4]
    assert fig.axes[0].get_lines()[0].get_color() == 'g'
    assert fig.axes[0].get_lines()[1].get_color() == 'k'
    assert fig.axes[0].get_lines()[1].get_linewidth() == 2
    assert fig.axes[0].get_lines()[1].get_linestyle() == '-'
    assert fig.axes[0].get_lines()[1].get_xdata().shape == (100,)
    assert fig.axes[0].get_lines()[1].get_ydata().shape == (100,)
    assert fig.axes[0].get_lines()[1].get_ydata().min() >= 0
    assert fig.axes[0].get_lines()[1].get_ydata().max() <= 0.45

    # Test case 2: mean = 1, std_dev = 2, num_samples = 500
    mean = 1
    std_dev = 2
    num_samples = 500
    samples, fig = task_func(mean, std_dev, num_samples)
    assert samples.shape == (num_samples,)
    assert fig is not None
    assert isinstance(fig, plt.Figure)
    assert fig.axes[0].get_title() == "Fit results: mean = 1.00,  std = 2.00"
    assert fig.axes[0].get_xlabel() == "Values"
    assert fig.axes[0].get_ylabel() == "Density"
    assert fig.axes[0].get_xlim() == (-5.5, 5.5)
    assert fig.axes[0].get_ylim() == (0, 0.045)
    assert fig.axes[0].get_xticks() == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert fig.axes[0].get_yticks() == [0, 0.01, 0.02, 0.03, 0.04]
    assert fig.axes[0].get_lines()[0].get_color() == 'g'
    assert fig.axes[0].get_lines()[1].get_color() == 'k'
    assert fig.axes[0].get_lines()[1].get_linewidth() == 2
    assert fig.axes[0].get_lines()[1].get_linestyle() == '-'
    assert fig.axes[0].get_lines()[1].get_xdata().shape == (100,)
    assert fig.axes[0].get_lines()[1].get_ydata().shape == (100,)
    assert fig.axes[0].get_lines()[1].get_ydata().min() >= 0
    assert fig.axes[0].get_lines()[1].get_ydata().max() <= 0.045