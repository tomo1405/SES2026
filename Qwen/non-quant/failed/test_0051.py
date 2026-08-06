import pytest
from src_0051 import task_func

def test_task_func():
    timestamp = 1633072800  # Example timestamp for 2021-10-01 00:00:00 UTC
    df, ax = task_func(timestamp)
    
    # Check if the DataFrame has the correct columns
    assert list(df.columns) == ["Timezone", "Datetime"]
    
    # Check if the DataFrame has the correct number of rows
    assert len(df) == len(TIMEZONES)
    
    # Check if the Datetime column is of datetime type
    assert pd.api.types.is_datetime64_any_dtype(df["Datetime"])
    
    # Check if the Timezone column contains the expected timezones
    assert all(tz in df["Timezone"].values for tz in TIMEZONES)
    
    # Check if the plot axis is not None
    assert ax is not None
    
    # Check if the plot title and labels are set correctly
    assert ax.get_title() == "Datetime = f(Timezone)"
    assert ax.get_ylabel() == "Datetime"
    assert ax.get_xlabel() == "Timezone"

# Run the tests
if __name__ == "__main__":
    pytest.main()