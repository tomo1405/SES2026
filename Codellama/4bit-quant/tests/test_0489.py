from datetime import datetime

import numpy as np
import pandas as pd


def test_task_func():
    start_time = 0
    end_time = 100
    step = 1
    amplitude = 10
    period = 10
    seed = 0

    np.random.seed(seed)

    if period <= 0 or step < 1:
        raise ValueError("Invalid input values")

    COLUMNS = ["Timestamp", "Value"]

    timestamps = np.arange(start_time, end_time, step)
    df = pd.DataFrame(columns=COLUMNS)

    if amplitude == 0:
        values = [0] * len(timestamps)
    else:
        values = np.random.normal(size=len(timestamps))

    data = []
    for i, ts in enumerate(timestamps):
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        value = values[i] + amplitude * np.sin(2 * np.pi * ts / period)
        data.append([dt, value])

    df = pd.DataFrame(data, columns=COLUMNS)

    ax = df.plot(x="Timestamp", y="Value", title="Time Series with Seasonality")
    ax.set_ylabel("Value")

    assert ax.get_title() == "Time Series with Seasonality"
    assert ax.get_xlabel() == "Timestamp"
    assert ax.get_ylabel() == "Value"

    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_label() == "Value"

    assert len(ax.get_xticks()) == len(timestamps)
    assert len(ax.get_yticks()) == len(values)

    assert ax.get_xticks()[0] == start_time
    assert ax.get_xticks()[-1] == end_time
    assert ax.get_yticks()[0] == 0
    assert ax.get_yticks()[-1] == amplitude

    assert ax.get_xticklabels()[0].get_text() == "00:00:00"
    assert ax.get_xticklabels()[-1].get_text() == "23:59:59"
    assert ax.get_yticklabels()[0].get_text() == "0"
    assert ax.get_yticklabels()[-1].get_text() == str(amplitude)

    assert ax.get_xlim() == (start_time, end_time)
    assert ax.get_ylim() == (0, amplitude)

    assert ax.get_xticks()[0] == start_time
    assert ax.get_xticks()[-1] == end_time
    assert ax.get_yticks()[0] == 0
    assert ax.get_yticks()[-1] == amplitude

    assert ax.get_xticklabels()[0].get_text() == "00:00:00"
    assert ax.get_xticklabels()[-1].get_text() == "23:59:59"
    assert ax.get_yticklabels()[0].get_text() == "0"
    assert ax.get_yticklabels()[-1].get_text() == str(amplitude)

    assert ax.get_xlim() == (start_time, end_time)
    assert ax.get_ylim() == (0, amplitude)