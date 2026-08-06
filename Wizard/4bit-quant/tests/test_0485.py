python
import math
import numpy as np
from datetime import datetime
import pandas as pd
import pytest

def task_func(
    start_time,
    end_time,
    step,
    columns=["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
    sensor_statuses=["OK", "MAINTENANCE_REQUIRED", "ERROR"],
    random_seed=42,
):
    np.random.seed(random_seed)

    if start_time > end_time:
        raise ValueError("start_time cannot be after end_time")
    if step < 0:
        raise ValueError("step must be positive")

    timestamps = list(range(start_time, end_time, step))

    data = []
    for ts in timestamps:
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1)
        sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1)
        sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1)
        status = np.random.choice(sensor_statuses)
        row = [dt, sensor1, sensor2, sensor3, status]
        data.append(row)

    return pd.DataFrame(data, columns=columns)

def test_task_func():
    # Test case 1: start_time > end_time
    with pytest.raises(ValueError):
        task_func(1000, 500, 100)

    # Test case 2: step < 0
    with pytest.raises(ValueError):
        task_func(500, 1000, -100)

    # Test case 3: normal case
    df = task_func(500, 1000, 100)
    assert df.shape == (10, 5)
    assert df.columns.tolist() == ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"]
    assert df["Timestamp"].tolist() == [
        "2022-01-01 00:00:00.000000",
        "2022-01-01 00:00:10.000000",
        "2022-01-01 00:00:20.000000",
        "2022-01-01 00:00:30.000000",
        "2022-01-01 00:00:40.000000",
        "2022-01-01 00:00:50.000000",
        "2022-01-01 00:01:00.000000",
        "2022-01-01 00:01:10.000000",
        "2022-01-01 00:01:20.000000",
        "2022-01-01 00:01:30.000000",
        "2022-01-01 00:01:40.000000",
    ]
    assert df["Sensor1"].tolist() == [
        0.5403023058681398,
        -0.7568024953079282,
        -0.9589242746631385,
        -0.3507832276896189,
        0.6536436208636119,
        -0.9899924966004454,
        -0.1411200080598672,
        -0.8912073600614258,
        -0.6536436208636119,
        -0.3507832276896189,
        0.5403023058681398,
    ]
    assert df["Sensor2"].tolist() == [
        0.8414709848078965,
        -0.5403023058681398,
        -0.3507832276896189,
        0.9589242746631385,
        -0.7568024953079282,
        -0.1411200080598672,
        0.9899924966004454,
        -0.8912073600614258,
        0.6536436208636119,
        -0.3507832276896189,
        0.8414709848078965,
    ]
    assert df["Sensor3"].tolist() == [
        -1.5574077246549072,
        -1.1411200080598672,
        0.3507832276896189,
        -1.3507832276896189,
        0.5403023058681398,
        -0.1411200080598672,
        -1.9899924966004454,
        0.8912073600614258,
        -0.6536436208636119,
        0.3507832276896189,
        -1.5574077246549072,
    ]
    assert df["SensorStatus"].tolist() == [
        "MAINTENANCE_REQUIRED",
        "OK",
        "ERROR",
        "OK",
        "MAINTENANCE_REQUIRED",
        "ERROR",
        "OK",
        "MAINTENANCE_REQUIRED",
        "OK",
        "ERROR",
        "MAINTENANCE_REQUIRED",
    ]