import pytest
from src_0050 import task_func

def test_task_func_with_valid_timestamps():
    timestamps = [1609459200, 1609545600, 1609632000]  # Example timestamps for January 1, 2, and 3, 2021
    df, ax = task_func(timestamps)
    
    assert isinstance(df, pd.DataFrame)
    assert "Timestamp" in df.columns
    assert "Datetime" in df.columns
    assert len(df) == len(timestamps)
    
    expected_dates = [
        "2021-01-01 00:00:00",
        "2021-01-02 00:00:00",
        "2021-01-03 00:00:00"
    ]
    assert all(df["Datetime"] == expected_dates)
    
    assert isinstance(ax, tuple)

def test_task_func_with_empty_timestamps():
    with pytest.raises(ValueError) as excinfo:
        task_func([])
    assert str(excinfo.value) == "Input list of timestamps is empty."

def test_task_func_with_single_timestamp():
    timestamps = [1609459200]  # Example timestamp for January 1, 2021
    df, ax = task_func(timestamps)
    
    assert isinstance(df, pd.DataFrame)
    assert "Timestamp" in df.columns
    assert "Datetime" in df.columns
    assert len(df) == len(timestamps)
    
    expected_date = ["2021-01-01 00:00:00"]
    assert all(df["Datetime"] == expected_date)
    
    assert isinstance(ax, tuple)