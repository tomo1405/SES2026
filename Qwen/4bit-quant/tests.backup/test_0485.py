import pytest
from src_0485 import task_func

def test_task_func_start_after_end():
    with pytest.raises(ValueError, match="start_time cannot be after end_time"):
        task_func(end_time=1609459200000, start_time=1609459260000)

def test_task_func_negative_step():
    with pytest.raises(ValueError, match="step must be positive"):
        task_func(start_time=1609459200000, end_time=1609459260000, step=-1)

def test_task_func_valid_input():
    df = task_func(start_time=1609459200000, end_time=1609459260000, step=60000)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert all(col in df.columns for col in ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"])

def test_task_func_timestamp_format():
    df = task_func(start_time=1609459200000, end_time=1609459260000, step=60000)
    assert all(isinstance(ts, str) and len(ts) == 26 for ts in df["Timestamp"])

def test_task_func_sensor_values():
    df = task_func(start_time=1609459200000, end_time=1609459260000, step=60000)
    assert all(isinstance(value, float) for value in df["Sensor1"])
    assert all(isinstance(value, float) for value in df["Sensor2"])
    assert all(isinstance(value, float) for value in df["Sensor3"])

def test_task_func_sensor_status():
    df = task_func(start_time=1609459200000, end_time=1609459260000, step=60000)
    assert all(status in ["OK", "MAINTENANCE_REQUIRED", "ERROR"] for status in df["SensorStatus"])

def test_task_func_random_seed():
    df1 = task_func(start_time=1609459200000, end_time=1609459260000, step=60000, random_seed=42)
    df2 = task_func(start_time=1609459200000, end_time=1609459260000, step=60000, random_seed=42)
    assert df1.equals(df2)