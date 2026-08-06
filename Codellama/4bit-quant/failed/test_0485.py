import pytest
from src_0485 import task_func

def test_task_func():
    # Test that the function returns a DataFrame with the correct columns
    df = task_func(0, 1000, 100)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"]

    # Test that the function raises an error if start_time is after end_time
    with pytest.raises(ValueError):
        task_func(1000, 0, 100)

    # Test that the function raises an error if step is negative
    with pytest.raises(ValueError):
        task_func(0, 1000, -100)

    # Test that the function returns a DataFrame with the correct number of rows
    df = task_func(0, 1000, 100)
    assert len(df) == 10

    # Test that the function returns a DataFrame with the correct values in the Timestamp column
    df = task_func(0, 1000, 100)
    assert df["Timestamp"].tolist() == [
        "1970-01-01 00:00:00.000000",
        "1970-01-01 00:00:01.000000",
        "1970-01-01 00:00:02.000000",
        "1970-01-01 00:00:03.000000",
        "1970-01-01 00:00:04.000000",
        "1970-01-01 00:00:05.000000",
        "1970-01-01 00:00:06.000000",
        "1970-01-01 00:00:07.000000",
        "1970-01-01 00:00:08.000000",
        "1970-01-01 00:00:09.000000",
    ]

    # Test that the function returns a DataFrame with the correct values in the Sensor1 column
    df = task_func(0, 1000, 100)
    assert df["Sensor1"].tolist() == [
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
        -0.9999999999999999,
    ]

    # Test that the function returns a DataFrame with the correct values in the Sensor2 column
    df = task_func(0, 1000, 100)
    assert df["Sensor2"].tolist() == [
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
    ]

    # Test that the function returns a DataFrame with the correct values in the Sensor3 column
    df = task_func(0, 1000, 100)
    assert df["Sensor3"].tolist() == [
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
        0.9999999999999999,
    ]

    # Test that the function returns a DataFrame with the correct values in the SensorStatus column
    df = task_func(0, 1000, 100)
    assert df["SensorStatus"].tolist() == [
        "OK",
        "OK",
        "OK",
        "OK",
        "OK",
        "OK",
        "OK",
        "OK",
        "OK",
        "OK",
    ]