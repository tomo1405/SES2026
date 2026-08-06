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
        task_func(1621234567890, 1621234567880, 1000)

    # Test case 2: step < 0
    with pytest.raises(ValueError):
        task_func(1621234567890, 1621234567990, -1000)

    # Test case 3: normal case
    df = task_func(1621234567890, 1621234567990, 1000)
    assert df.shape == (10, 5)
    assert df.iloc[0]["Timestamp"] == "2021-05-12 13:42:47.890000"
    assert df.iloc[9]["Timestamp"] == "2021-05-12 13:42:57.890000"
    assert df.iloc[0]["Sensor1"] == pytest.approx(0.8414709848078965)
    assert df.iloc[9]["Sensor1"] == pytest.approx(-0.8414709848078965)
    assert df.iloc[0]["Sensor2"] == pytest.approx(0.5403023058681398)
    assert df.iloc[9]["Sensor2"] == pytest.approx(-0.5403023058681398)
    assert df.iloc[0]["Sensor3"] == pytest.approx(1.5574077246549023)
    assert df.iloc[9]["Sensor3"] == pytest.approx(-1.5574077246549023)
    assert df.iloc[0]["SensorStatus"] in ["OK", "MAINTENANCE_REQUIRED", "ERROR"]
    assert df.iloc[9]["SensorStatus"] in ["OK", "MAINTENANCE_REQUIRED", "ERROR"]