python
import pandas as pd
from datetime import datetime
import pytest

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

def test_task_func():
    # Test case 1: Valid date string and valid booking data
    date_str = "2022-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Booked", "Room3": "Booked"}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.shape == (5, 2)
    assert ax.get_title() == "Booking Statuses for 2022-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["Booked", "Not Booked"]
    assert ax.get_xticks() == [0, 1]
    assert ax.get_ylim() == (0, 2)
    assert ax.get_yticks() == [0, 1, 2]
    assert ax.get_yticklabels() == ["0", "1", "2"]

    # Test case 2: Invalid date string
    date_str = "2021-01-01"
    with pytest.raises(ValueError) as e:
        task_func(date_str, booking_data)
    assert str(e.value) == "Invalid date: Date is in the past. Please provide a future date."

    # Test case 3: Empty booking data
    date_str = "2022-01-01"
    booking_data = {}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.shape == (5, 2)
    assert ax.get_title() == "Booking Statuses for 2022-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xticklabels() == ["Not Listed", "Not Listed"]
    assert ax.get_xticks() == [0, 1]
    assert ax.get_ylim() == (0, 2)
    assert ax.get_yticks() == [0, 1, 2]
    assert ax.get_yticklabels() == ["0", "1", "2"]

    # Test case 4: Invalid booking data
    date_str = "2022-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Invalid", "Room3": "Booked"}
    with pytest.raises(ValueError) as e:
        task_func(date_str, booking_data)
    assert str(e.value) == "Invalid booking data: Room2"