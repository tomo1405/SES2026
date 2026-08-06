import pytest
from src_1049 import task_func
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_valid_date():
    ax = task_func("2023-10-15")
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Sine Wave for 2023-10-15 (Frequency: 15)"

def test_task_func_invalid_date():
    with pytest.raises(ValueError):
        task_func("2023-13-01")

def test_task_func_sine_wave_properties():
    ax = task_func("2023-01-01")
    lines = ax.get_lines()
    assert len(lines) == 1
    xdata, ydata = lines[0].get_data()
    assert np.allclose(xdata, np.linspace(0, 2 * np.pi, 1000))
    assert np.allclose(ydata, np.sin(1 * xdata))

def test_task_func_plot_output():
    ax = task_func("2023-01-01")
    fig = ax.get_figure()
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert image_base64.startswith('iVBORw0KGgoAAAANSUhEUgAA')