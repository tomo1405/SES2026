import pytest
from src_0485 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_start_time_after_end_time():
    with pytest.raises(ValueError, match="start_time cannot be after end_time"):
        task_func(end_time=1000, start_time=2000, step=100)

def test_task_func_negative_step():
    with pytest.raises(ValueError, match="step must be positive"):
        task_func(start_time=1000, end_time=2000, step=-100)

def test_task_func_valid_input():
    df = task_func(start_time=1000, end_time=2000, step=100)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"]
    assert len(df) == (2000 - 1000) // 100

def test_task_func_timestamp_format():
    df = task_func(start_time=1000, end_time=2000, step=100)
    for timestamp in df["Timestamp"]:
        datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")

def test_task_func_sensor_values():
    df = task_func(start_time=1000, end_time=2000, step=100)
    for index, row in df.iterrows():
        ts = row["Timestamp"]
        dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f").timestamp() * 1000
        assert math.isclose(row["Sensor1"], math.sin(dt / 1000), rel_tol=0.1)
        assert math.isclose(row["Sensor2"], math.cos(dt / 1000), rel_tol=0.1)
        assert math.isclose(row["Sensor3"], math.tan(dt / 1000), rel_tol=0.1)

def test_task_func_sensor_status():
    df = task_func(start_time=1000, end_time=2000, step=100)
    assert all(status in ["OK", "MAINTENANCE_REQUIRED", "ERROR"] for status in df["SensorStatus"])