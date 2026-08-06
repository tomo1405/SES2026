import pytest
from src_0449 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_default_parameters():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    x = np.linspace(-3, 3, 100)
    y = np.exp(-0.5 * (x ** 2))
    np.testing.assert_almost_equal(ax.lines[0].get_ydata(), y)

def test_task_func_custom_parameters():
    ax = task_func(mu=2, sigma=0.5)
    assert isinstance(ax, plt.Axes)
    x = np.linspace(0.5, 3.5, 100)
    y = np.exp(-0.5 * ((x - 2) / 0.5) ** 2) / (0.5 * np.sqrt(2 * np.pi))
    np.testing.assert_almost_equal(ax.lines[0].get_ydata(), y)

def test_task_func_plot_content():
    ax = task_func()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    # Here you would typically compare the image content to a known good image,
    # but for simplicity, we just check that the plot is not empty.
    assert len(image_base64) > 0

def test_task_func_no_show_plot():
    ax = task_func()
    # Ensure that the plot is not shown by default
    with pytest.raises(AssertionError):
        plt.show()