import pytest
from src_0051 import task_func

def test_task_func():
    # Test with a specific timestamp
    timestamp = 1672531200  # Example timestamp for January 1, 2023, 00:00:00 UTC
    df, ax = task_func(timestamp)
    
    # Check if the DataFrame has the correct columns
    assert "Timezone" in df.columns
    assert "Datetime" in df.columns
    
    # Check if the DataFrame has the correct number of rows
    assert len(df) == len(TIMEZONES)
    
    # Check if the Datetime column is of datetime type
    assert pd.api.types.is_datetime64_any_dtype(df["Datetime"])
    
    # Check if the plot is created and closed
    assert ax is not None
    assert plt.fignum_exists(1) is False  # Ensure the figure is closed

    # Check if the DataFrame contains the correct timezone information
    for tz in TIMEZONES:
        assert tz in df["Timezone"].values

    # Check if the DataFrame contains the correct datetime information
    expected_dates = [
        "2023-01-01 19:00:00",  # New York
        "2023-01-01 15:00:00",  # London
        "2023-01-02 02:00:00",  # Shanghai
        "2023-01-02 03:00:00",  # Tokyo
        "2023-01-02 08:00:00",  # Sydney
    ]
    for date in expected_dates:
        assert date in df["Datetime"].dt.strftime(DATE_FORMAT).values