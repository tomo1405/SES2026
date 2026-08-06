import pytest
from src_1045 import task_func

def test_task_func_valid_date():
    date_str = "2023-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Listed", "Room3": "Booked"}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.shape == (3, 2)
    assert report_df["Room"].tolist() == ROOMS
    assert report_df["Booking Status"].tolist() == ["Booked", "Not Listed", "Booked"]
    assert ax.get_title() == "Booking Statuses for 2023-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"

def test_task_func_invalid_date():
    date_str = "2023-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Listed", "Room3": "Booked"}
    with pytest.raises(ValueError):
        task_func(date_str, booking_data)

def test_task_func_invalid_booking_data():
    date_str = "2023-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Listed", "Room3": "Booked"}
    with pytest.raises(ValueError):
        task_func(date_str, booking_data)