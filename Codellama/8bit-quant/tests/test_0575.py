import matplotlib.pyplot as plt
import numpy as np
from src_0575 import task_func


def test_task_func():
    # Test that the function returns a matplotlib axis object
    ax = task_func()
    assert isinstance(ax, plt.Axes)

    # Test that the function plots the data and the fit correctly
    x = np.linspace(0, 4*np.pi, 100)
    y = np.sin(x) + 0.2 * np.random.rand(100)
    expected_fit = np.sin(x)
    assert np.allclose(ax.lines[0].get_data()[1], y)
    assert np.allclose(ax.lines[1].get_data()[1], expected_fit)

    # Test that the function sets the correct labels and legend
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_legend().get_texts()[0].get_text() == 'data'
    assert ax.get_legend().get_texts()[1].get_text() == 'fit: a=1.000, b=1.000'