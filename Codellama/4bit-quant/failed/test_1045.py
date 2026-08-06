import pytest
from src_1045 import task_func

def test_task_func():
    # Test 1: Valid date string
    date_str = "2023-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Booked", "Room3": "Booked"}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.equals(pd.DataFrame({"Room": ["Room1", "Room2", "Room3"], "Booking Status": ["Booked", "Not Booked", "Booked"]}))
    assert ax.get_title() == "Booking Statuses for 2023-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"

    # Test 2: Invalid date string
    date_str = "2023-01-01"
    booking_data = {"Room1": "Booked", "Room2": "Not Booked", "Room3": "Booked"}
    with pytest.raises(ValueError):
        task_func(date_str, booking_data)

    # Test 3: Valid date string, but no booking data
    date_str = "2023-01-01"
    booking_data = {}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.equals(pd.DataFrame({"Room": ["Room1", "Room2", "Room3"], "Booking Status": ["Not Listed", "Not Listed", "Not Listed"]}))
    assert ax.get_title() == "Booking Statuses for 2023-01-01"
    assert ax.get_xlabel() == "Booking Status"
    assert ax.get_ylabel() == "Count"