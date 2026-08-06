import pytest
import math
import numpy as np
from datetime import datetime
import pandas as pd

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
    # Test case 1: Check if ValueError is raised when start_time is greater than end_time
    with pytest.raises(ValueError):
        task_func(start_time=100, end_time=50, step=1)

    # Test case 2: Check if ValueError is raised when step is negative
    with pytest.raises(ValueError):
        task_func(start_time=0, end_time=100, step=-1)

    # Test case 3: Check if the returned DataFrame has the correct number of rows
    df = task_func(start_time=0, end_time=1000, step=1)
    assert len(df) == 1000

    # Test case 4: Check if the returned DataFrame has the correct column names
    df = task_func(start_time=0, end_time=1000, step=1)
    assert list(df.columns) == ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"]

    # Test case 5: Check if the returned DataFrame has the correct data types
    df = task_func(start_time=0, end_time=1000, step=1)
    assert df["Timestamp"].dtype == "object"
    assert df["Sensor1"].dtype == "float64"
    assert df["Sensor2"].dtype == "float64"
    assert df["Sensor3"].dtype == "float64"
    assert df["SensorStatus"].dtype == "object"