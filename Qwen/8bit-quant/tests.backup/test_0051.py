import pytest
from src_0051 import task_func
import pandas as pd
from datetime import datetime

def test_task_func():
    # Test with a known timestamp
    timestamp = 1633072800  # October 1, 2021, 00:00:00 UTC
    df, ax = task_func(timestamp)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (5, 2), "DataFrame should have 5 rows and 2 columns"
    
    # Check if the DataFrame contains the correct timezones
    expected_timezones = [
        "America/New_York",
        "Europe/London",
        "Asia/Shanghai",
        "Asia/Tokyo",
        "Australia/Sydney",
    ]
    assert all(df["Timezone"] == expected_timezones), "Timezones in DataFrame are incorrect"
    
    # Check if the DataFrame contains the correct datetimes
    expected_datetimes = [
        "2021-10-01 19:00:00",  # New York
        "2021-10-01 05:00:00",  # London
        "2021-10-01 17:00:00",  # Shanghai
        "2021-10-01 18:00:00",  # Tokyo
        "2021-10-01 18:00:00",  # Sydney
    ]
    assert all(df["Datetime"].dt.strftime("%Y-%m-%d %H:%M:%S") == expected_datetimes), "Datetimes in DataFrame are incorrect"
    
    # Check if the plot axis is of the correct type
    assert isinstance(ax, plt.Axes), "Return value 'ax' should be an instance of matplotlib.axes.Axes"

# Run the tests
if __name__ == "__main__":
    pytest.main()