import pytest
from src_1074 import task_func
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_valid_times():
    time_strings = [
        "01/01/2023 12:00:00.000000",
        "01/01/2023 12:01:00.000000",
        "01/01/2023 12:02:00.000000"
    ]
    ax = task_func(time_strings)
    assert ax is not None
    assert len(ax.patches) == 60  # 60 bins for seconds in a minute

def test_task_func_invalid_times():
    time_strings = [
        "01/01/2023 12:00:00.000000",
        "01/01/2023 12:01:00.000000",
        "invalid_time"
    ]
    ax = task_func(time_strings)
    assert ax is None

def test_task_func_empty_list():
    time_strings = []
    ax = task_func(time_strings)
    assert ax is not None
    assert len(ax.patches) == 0  # No data to plot

def test_task_func_single_time():
    time_strings = ["01/01/2023 12:00:00.000000"]
    ax = task_func(time_strings)
    assert ax is not None
    assert len(ax.patches) == 60  # 60 bins for seconds in a minute

def test_task_func_custom_format():
    time_strings = [
        "01-01-2023 12:00:00.000000",
        "01-01-2023 12:01:00.000000",
        "01-01-2023 12:02:00.000000"
    ]
    time_format = "%d-%m-%Y %H:%M:%S.%f"
    ax = task_func(time_strings, time_format=time_format)
    assert ax is not None
    assert len(ax.patches) == 60  # 60 bins for seconds in a minute

def test_task_func_plot_output():
    time_strings = [
        "01/01/2023 12:00:00.000000",
        "01/01/2023 12:01:00.000000",
        "01/01/2023 12:02:00.000000"
    ]
    ax = task_func(time_strings)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert image_base64  # Ensure that the plot is generated and saved correctly