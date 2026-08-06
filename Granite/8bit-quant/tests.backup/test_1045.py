import pandas as pd
from datetime import datetime
from unittest.mock import patch
from src_1045 import task_func
import pytest

@pytest.fixture
def mock_datetime():
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2023, 5, 10)
        yield mock_datetime

def test_task_func_with_valid_date(mock_datetime):
    date_str = "2023-05-11"
    booking_data = {"Room1": "Booked", "Room2": "Available"}
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.shape == (5, 2)
    assert ax.get_title() == "Booking Statuses for 2023-05-11"

def test_task_func_with_invalid_date(mock_datetime):
    date_str = "2023-05-09"
    booking_data = {"Room1": "Booked", "Room2": "Available"}
    with pytest.raises(ValueError, match="Date is in the past"):
        task_func(date_str, booking_data)

def test_task_func_with_invalid_date_format(mock_datetime):
    date_str = "2023-05-11-invalid"
    booking_data = {"Room1": "Booked", "Room2": "Available"}
    with pytest.raises(ValueError, match="Invalid date"):
        task_func(date_str, booking_data)