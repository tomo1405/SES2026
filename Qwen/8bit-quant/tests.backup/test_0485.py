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
    assert len(df) == 11  # (2000 - 1000) / 100 + 1

def test_task_func_timestamp_format():
    df = task_func(start_time=1000, end_time=2000, step=1000)
    for timestamp in df["Timestamp"]:
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        assert isinstance(dt, datetime)

def test_task_func_sensor_values():
    df = task_func(start_time=1000, end_time=2000, step=1000)
    for index, row in df.iterrows():
        sensor1 = row["Sensor1"]
        sensor2 = row["Sensor2"]
        sensor3 = row["Sensor3"]
        ts = int(datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S.%f").timestamp() * 1000)
        assert abs(sensor1 - (math.sin(ts / 1000) + np.random.normal(0, 0.1))) < 0.2
        assert abs(sensor2 - (math.cos(ts / 1000) + np.random.normal(0, 0.1))) < 0.2
        assert abs(sensor3 - (math.tan(ts / 1000) + np.random.normal(0, 0.1))) < 0.2

def test_task_func_sensor_status():
    df = task_func(start_time=1000, end_time=2000, step=1000)
    for status in df["SensorStatus"]:
        assert status in ["OK", "MAINTENANCE_REQUIRED", "ERROR"]

def test_task_func_random_seed_consistency():
    df1 = task_func(start_time=1000, end_time=2000, step=100, random_seed=42)
    df2 = task_func(start_time=1000, end_time=2000, step=100, random_seed=42)
    assert df1.equals(df2)