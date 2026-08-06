import pytest
from src_0489 import task_func

def test_task_func_invalid_period():
    with pytest.raises(ValueError):
        task_func(0, 1000, 1, 1, 0)

def test_task_func_invalid_step():
    with pytest.raises(ValueError):
        task_func(0, 1000, 0, 1, 1000)

def test_task_func_zero_amplitude():
    ax = task_func(0, 1000, 1, 0, 1000)
    assert len(ax.lines) == 1
    assert all(value == 0 for value in ax.lines[0].get_ydata())

def test_task_func_non_zero_amplitude():
    ax = task_func(0, 1000, 1, 1, 1000)
    assert len(ax.lines) == 1
    assert not all(value == 0 for value in ax.lines[0].get_ydata())

def test_task_func_timestamps():
    ax = task_func(0, 1000, 1, 1, 1000)
    timestamps = [datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f") for ts in range(0, 1000, 1)]
    assert list(ax.get_lines()[0].get_xdata()) == timestamps

def test_task_func_values():
    ax = task_func(0, 1000, 1, 1, 1000)
    values = [np.random.normal() + np.sin(2 * np.pi * ts / 1000) for ts in range(0, 1000, 1)]
    assert np.allclose(ax.get_lines()[0].get_ydata(), values, atol=1e-5)

def test_task_func_plot_title():
    ax = task_func(0, 1000, 1, 1, 1000)
    assert ax.get_title() == "Time Series with Seasonality"

def test_task_func_plot_ylabel():
    ax = task_func(0, 1000, 1, 1, 1000)
    assert ax.get_ylabel() == "Value"