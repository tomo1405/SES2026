import pytest
from src_0485 import task_func

def test_task_func():
    start_time = 1609459200000
    end_time = 1609459300000
    step = 1000
    expected_columns = ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"]
    expected_sensor_statuses = ["OK", "MAINTENANCE_REQUIRED", "ERROR"]
    random_seed = 42
    df = task_func(start_time, end_time, step, random_seed=random_seed)
    assert df.columns.tolist() == expected_columns
    assert df["SensorStatus"].unique().tolist() == expected_sensor_statuses

def test_task_func_invalid_start_time():
    with pytest.raises(ValueError) as excinfo:
        task_func(end_time=1609459300000, start_time=1609459200000, step=1000)
    assert "start_time cannot be after end_time" in str(excinfo.value)

def test_task_func_invalid_step():
    with pytest.raises(ValueError) as excinfo:
        task_func(end_time=1609459300000, start_time=1609459200000, step=-1000)
    assert "step must be positive" in str(excinfo.value)