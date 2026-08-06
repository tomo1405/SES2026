import pandas as pd
import pytest
from src_1045 import task_func


def test_task_func_valid_date():
    date_str = "2023-12-25"
    booking_data = {"Room1": "Booked", "Room3": "Available"}
    report_df, ax = task_func(date_str, booking_data)
    
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 2)
    assert all(col in report_df.columns for col in ["Room", "Booking Status"])
    assert report_df.iloc[0]["Room"] == "Room1"
    assert report_df.iloc[0]["Booking Status"] == "Booked"
    assert report_df.iloc[1]["Booking Status"] == "Not Listed"
    assert report_df.iloc[3]["Booking Status"] == "Available"
    assert report_df.iloc[4]["Booking Status"] == "Not Listed"

def test_task_func_past_date():
    date_str = "2022-12-25"
    booking_data = {}
    with pytest.raises(ValueError, match="Date is in the past. Please provide a future date."):
        task_func(date_str, booking_data)

def test_task_func_invalid_date_format():
    date_str = "25-12-2023"
    booking_data = {}
    with pytest.raises(ValueError, match="Invalid date: "):
        task_func(date_str, booking_data)

def test_task_func_empty_booking_data():
    date_str = "2023-12-25"
    booking_data = {}
    report_df, ax = task_func(date_str, booking_data)
    
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 2)
    assert all(col in report_df.columns for col in ["Room", "Booking Status"])
    assert all(status == "Not Listed" for status in report_df["Booking Status"])

def test_task_func_all_rooms_booked():
    date_str = "2023-12-25"
    booking_data = {room: "Booked" for room in ROOMS}
    report_df, ax = task_func(date_str, booking_data)
    
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 2)
    assert all(col in report_df.columns for col in ["Room", "Booking Status"])
    assert all(status == "Booked" for status in report_df["Booking Status"])

def test_task_func_single_room_booked():
    date_str = "2023-12-25"
    booking_data = {"Room1": "Booked"}
    report_df, ax = task_func(date_str, booking_data)
    
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (5, 2)
    assert all(col in report_df.columns for col in ["Room", "Booking Status"])
    assert report_df.iloc[0]["Booking Status"] == "Booked"
    assert all(status == "Not Listed" for i, status in enumerate(report_df["Booking Status"]) if i != 0)