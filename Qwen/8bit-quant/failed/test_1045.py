import pytest
from src_1045 import task_func
from datetime import datetime
import pandas as pd

def test_task_func_valid_date():
    date_str = (datetime.now() + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    booking_data = {"Room1": "Booked", "Room3": "Available"}
    report_df, ax = task_func(date_str, booking_data)

    assert isinstance(report_df, pd.DataFrame)
    assert list(report_df.columns) == ["Room", "Booking Status"]
    assert len(report_df) == 5
    assert report_df.iloc[0]["Room"] == "Room1"
    assert report_df.iloc[0]["Booking Status"] == "Booked"
    assert report_df.iloc[2]["Room"] == "Room3"
    assert report_df.iloc[2]["Booking Status"] == "Available"
    assert report_df.iloc[4]["Room"] == "Room5"
    assert report_df.iloc[4]["Booking Status"] == "Not Listed"

def test_task_func_past_date():
    date_str = (datetime.now() - pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    booking_data = {"Room1": "Booked", "Room3": "Available"}

    with pytest.raises(ValueError, match="Date is in the past. Please provide a future date."):
        task_func(date_str, booking_data)

def test_task_func_invalid_date_format():
    date_str = "2023-13-01"
    booking_data = {"Room1": "Booked", "Room3": "Available"}

    with pytest.raises(ValueError, match="Invalid date: day is out of range for month"):
        task_func(date_str, booking_data)

def test_task_func_no_booking_data():
    date_str = (datetime.now() + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    booking_data = {}
    report_df, ax = task_func(date_str, booking_data)

    assert isinstance(report_df, pd.DataFrame)
    assert list(report_df.columns) == ["Room", "Booking Status"]
    assert len(report_df) == 5
    for i in range(5):
        assert report_df.iloc[i]["Room"] == ROOMS[i]
        assert report_df.iloc[i]["Booking Status"] == "Not Listed"