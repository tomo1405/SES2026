from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np


def test_task_func():
    date_str = "2022-01-01"
    date = datetime.strptime(date_str, "%Y-%m-%d")
    x = np.linspace(0, 2 * np.pi, 1000)
    frequency = date.day
    y = np.sin(frequency * x)
    _, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Sine Wave for {date_str} (Frequency: {frequency})")
    assert ax.get_title() == f"Sine Wave for {date_str} (Frequency: {frequency})"
    assert np.allclose(ax.get_xlim(), (0, 2 * np.pi))
    assert np.allclose(ax.get_ylim(), (-1, 1))
    assert np.allclose(ax.get_xticks(), np.linspace(0, 2 * np.pi, 11))
    assert np.allclose(ax.get_yticks(), np.linspace(-1, 1, 5))
    assert np.allclose(ax.get_xticklabels(), np.linspace(0, 2 * np.pi, 11))
    assert np.allclose(ax.get_yticklabels(), np.linspace(-1, 1, 5))
    assert np.allclose(ax.get_xlabel(), "X Axis")
    assert np.allclose(ax.get_ylabel(), "Y Axis")
    assert np.allclose(ax.get_title(), f"Sine Wave for {date_str} (Frequency: {frequency})")