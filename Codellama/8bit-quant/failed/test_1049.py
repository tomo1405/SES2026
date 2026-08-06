import pytest
from src_1049 import task_func
import datetime
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    date_str = "2022-01-01"
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    x = np.linspace(0, 2 * np.pi, 1000)
    frequency = date.day
    y = np.sin(frequency * x)
    _, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Sine Wave for {date_str} (Frequency: {frequency})")
    assert ax.get_title() == f"Sine Wave for {date_str} (Frequency: {frequency})"
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_xlim() == (0, 2 * np.pi)
    assert ax.get_ylim() == (-1, 1)
    assert ax.get_xticks() == np.linspace(0, 2 * np.pi, 11)
    assert ax.get_yticks() == np.linspace(-1, 1, 11)
    assert ax.get_xticklabels() == [f"{x:.2f}" for x in np.linspace(0, 2 * np.pi, 11)]
    assert ax.get_yticklabels() == [f"{y:.2f}" for y in np.linspace(-1, 1, 11)]
    assert ax.get_lines()[0].get_xdata() == x
    assert ax.get_lines()[0].get_ydata() == y
    assert ax.get_lines()[0].get_label() == "Sine Wave"
    assert ax.get_legend().get_title().get_text() == "Legend"
    assert ax.get_legend().get_texts()[0].get_text() == "Sine Wave"