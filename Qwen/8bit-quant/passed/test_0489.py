import pytest
from src_0489 import task_func

def test_task_func_invalid_period():
    with pytest.raises(ValueError):
        task_func(start_time=0, end_time=1000, step=100, amplitude=1, period=-1)

def test_task_func_invalid_step():
    with pytest.raises(ValueError):
        task_func(start_time=0, end_time=1000, step=0, amplitude=1, period=100)

def test_task_func_zero_amplitude():
    ax = task_func(start_time=0, end_time=1000, step=100, amplitude=0, period=100)
    df = ax.get_lines()[0].get_data()
    assert all(value == 0 for value in df[1])

def test_task_func_non_zero_amplitude():
    ax = task_func(start_time=0, end_time=1000, step=100, amplitude=1, period=100)
    df = ax.get_lines()[0].get_data()
    assert any(value != 0 for value in df[1])

def test_task_func_timestamp_format():
    ax = task_func(start_time=0, end_time=1000, step=100, amplitude=1, period=100)
    df = ax.get_lines()[0].get_data()
    for timestamp in df[0]:
        assert isinstance(timestamp, str)
        assert len(timestamp) == 26  # Format: YYYY-MM-DD HH:MM:SS.SSSSSS

def test_task_func_plot_title():
    ax = task_func(start_time=0, end_time=1000, step=100, amplitude=1, period=100)
    assert ax.get_title() == "Time Series with Seasonality"

def test_task_func_plot_ylabel():
    ax = task_func(start_time=0, end_time=1000, step=100, amplitude=1, period=100)
    assert ax.get_ylabel() == "Value"