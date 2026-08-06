python
import pandas as pd
import pytest
from datetime import datetime

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

def task_func(date_str, booking_data):
    # Validate the date string
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date < datetime.now():
            raise ValueError("Date is in the past. Please provide a future date.")
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}") from e

    report_data = [[room, booking_data.get(room, "Not Listed")] for room in ROOMS]
    report_df = pd.DataFrame(report_data, columns=["Room", "Booking Status"])

    # Create a bar plot of the booking statuses
    ax = (
        report_df["Booking Status"]
        .value_counts()
        .plot(kind="bar", title="Booking Statuses for " + date_str)
    )

    return report_df, ax

# Test cases
def test_task_func_valid_date():
    date_str = "2022-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Listed", "Room3": "Booked"}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.shape == (5, 2)
    assert ax.get_title() == "Booking Statuses for 2022-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["Booked", "Not Listed"]
    assert ax.get_ylim() == (0, 2)
    assert report_df.loc[0, "Booking Status"] == "Booked"
    assert report_df.loc[1, "Booking Status"] == "Not Listed"
    assert report_df.loc[2, "Booking Status"] == "Booked"
    assert report_df.loc[3, "Booking Status"] == "Not Listed"
    assert report_df.loc[4, "Booking Status"] == "Not Listed"

def test_task_func_invalid_date():
    date_str = "2021-12-31"
    booking_data = {"Room1": "Booked", "Room2": "Not Listed", "Room3": "Booked"}
    with pytest.raises(ValueError) as e:
        task_func(date_str, booking_data)
    assert str(e.value) == "Invalid date: Date is in the past. Please provide a future date."

def test_task_func_empty_booking_data():
    date_str = "2022-01-01"
    booking_data = {}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.shape == (5, 2)
    assert ax.get_title() == "Booking Statuses for 2022-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["Not Listed"]
    assert ax.get_ylim() == (0, 1)
    assert report_df.loc[0, "Booking Status"] == "Not Listed"
    assert report_df.loc[1, "Booking Status"] == "Not Listed"
    assert report_df.loc[2, "Booking Status"] == "Not Listed"
    assert report_df.loc[3, "Booking Status"] == "Not Listed"
    assert report_df.loc[4, "Booking Status"] == "Not Listed"

def test_task_func_missing_room():
    date_str = "2022-01-01"
    booking_data = {"Room1": "Booked", "Room3": "Booked"}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.shape == (5, 2)
    assert ax.get_title() == "Booking Statuses for 2022-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["Booked", "Not Listed"]
    assert ax.get_ylim() == (0, 2)
    assert report_df.loc[0, "Booking Status"] == "Booked"
    assert report_df.loc[1, "Booking Status"] == "Not Listed"
    assert report_df.loc[2, "Booking Status"] == "Booked"
    assert report_df.loc[3, "Booking Status"] == "Not Listed"
    assert report_df.loc[4, "Booking Status"] == "Not Listed"