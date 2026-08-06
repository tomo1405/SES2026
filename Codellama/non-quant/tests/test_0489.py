from datetime import datetime

import numpy as np
import pandas as pd
import pytest
from src_0489 import task_func


def test_task_func_valid_inputs():
    start_time = 0
    end_time = 100
    step = 1
    amplitude = 10
    period = 10
    seed = 0

    np.random.seed(seed)
    expected_timestamps = np.arange(start_time, end_time, step)
    expected_values = np.random.normal(size=len(expected_timestamps))
    expected_data = []
    for i, ts in enumerate(expected_timestamps):
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        value = expected_values[i] + amplitude * np.sin(2 * np.pi * ts / period)
        expected_data.append([dt, value])

    expected_df = pd.DataFrame(expected_data, columns=["Timestamp", "Value"])

    ax = task_func(start_time, end_time, step, amplitude, period, seed)

    assert np.allclose(ax.get_xdata(), expected_df["Timestamp"])
    assert np.allclose(ax.get_ydata(), expected_df["Value"])

def test_task_func_invalid_inputs():
    start_time = 0
    end_time = 100
    step = 1
    amplitude = 10
    period = 0
    seed = 0

    np.random.seed(seed)
    expected_timestamps = np.arange(start_time, end_time, step)
    expected_values = np.random.normal(size=len(expected_timestamps))
    expected_data = []
    for i, ts in enumerate(expected_timestamps):
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        value = expected_values[i] + amplitude * np.sin(2 * np.pi * ts / period)
        expected_data.append([dt, value])

    expected_df = pd.DataFrame(expected_data, columns=["Timestamp", "Value"])

    with pytest.raises(ValueError):
        task_func(start_time, end_time, step, amplitude, period, seed)