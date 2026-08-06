import pandas as pd
from datetime import datetime
from pytest import raises

from src_1045 import task_func

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

def test_task_func():
    date_str = "2023-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Listed"}
    report_df, ax = task_func(date_str, booking_data)

    assert report_df.shape == (5, 2)
    assert report_df["Room"].tolist() == ROOMS
    assert report_df["Booking Status"].tolist() == ["Booked", "Not Listed"] * 2
    assert ax.get_title() == "Booking Statuses for 2023-01-01"

def test_invalid_date():
    date_str = "2022-12-31"
    booking_data = {}
    with raises(ValueError, match="Date is in the past"):
        task_func(date_str, booking_data)

def test_invalid_date_format():
    date_str = "2023-01-01"
    booking_data = {}
    with raises(ValueError, match="Invalid date: unconverted data remains"):
        task_func(date_str, booking_data)