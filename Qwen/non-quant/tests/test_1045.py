import pytest
from src_1045 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_valid_date():
    date_str = "2024-12-25"
    booking_data = {"Room1": "Booked", "Room3": "Available"}
    report_df, ax = task_func(date_str, booking_data)
    
    assert isinstance(report_df, pd.DataFrame)
    assert list(report_df.columns) == ["Room", "Booking Status"]
    assert len(report_df) == 5
    assert report_df.loc[report_df["Room"] == "Room1", "Booking Status"].values[0] == "Booked"
    assert report_df.loc[report_df["Room"] == "Room2", "Booking Status"].values[0] == "Not Listed"
    assert report_df.loc[report_df["Room"] == "Room3", "Booking Status"].values[0] == "Available"
    assert report_df.loc[report_df["Room"] == "Room4", "Booking Status"].values[0] == "Not Listed"
    assert report_df.loc[report_df["Room"] == "Room5", "Booking Status"].values[0] == "Not Listed"

def test_task_func_past_date():
    with pytest.raises(ValueError, match="Date is in the past"):
        task_func("2020-01-01", {})

def test_task_func_invalid_date_format():
    with pytest.raises(ValueError, match="Invalid date"):
        task_func("25-12-2024", {})

def test_task_func_no_bookings():
    date_str = "2024-12-25"
    booking_data = {}
    report_df, ax = task_func(date_str, booking_data)
    
    assert all(report_df["Booking Status"] == "Not Listed")

def test_task_func_all_rooms_booked():
    date_str = "2024-12-25"
    booking_data = {room: "Booked" for room in ["Room1", "Room2", "Room3", "Room4", "Room5"]}
    report_df, ax = task_func(date_str, booking_data)
    
    assert all(report_df["Booking Status"] == "Booked")