import pytest
from src_0485 import task_func
import numpy as np
import math
from datetime import datetime
import pandas as pd

def test_task_func():
    start_time = 1000
    end_time = 2000
    step = 100
    columns = ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"]
    sensor_statuses = ["OK", "MAINTENANCE_REQUIRED", "ERROR"]
    random_seed = 42

    result = task_func(start_time, end_time, step, columns, sensor_statuses, random_seed)

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (11, 5)
    assert result.columns.tolist() == columns
    assert result["Timestamp"].dtype == np.dtype("datetime64[ns]")
    assert result["Sensor1"].dtype == np.dtype("float64")
    assert result["Sensor2"].dtype == np.dtype("float64")
    assert result["Sensor3"].dtype == np.dtype("float64")
    assert result["SensorStatus"].dtype == np.dtype("object")
    assert result["SensorStatus"].unique().tolist() == sensor_statuses

    for i in range(11):
        ts = start_time + i * step
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1)
        sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1)
        sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1)
        status = np.random.choice(sensor_statuses)
        row = [dt, sensor1, sensor2, sensor3, status]
        assert result.iloc[i].tolist() == row