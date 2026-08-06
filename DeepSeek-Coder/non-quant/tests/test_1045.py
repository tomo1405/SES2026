import pytest
from src_1045 import task_func
from datetime import datetime
import pandas as pd

# Mock data for testing
booking_data = {
    "Room1": "Booked",
    "Room2": "Not Booked",
    "Room3": "Booked",
    "Room4": "Not Booked",
    "Room5": "Booked"
}

def test_task_func():
    # Test with a future date
    date_str = "2024-05-01"
    report_df, ax = task_func(date_str, booking_data)
    
    # Assertions
    assert isinstance(report_df, pd.DataFrame), "The report_df should be a DataFrame"
    assert len(report_df) == len(ROOMS), "The number of rows should match the number of rooms"
    assert "Booked" in report_df["Booking Status"].values, "The report should include booked rooms"
    assert "Not Booked" in report_df["Booking Status"].values, "The report should include not booked rooms"

    # Add more assertions as needed to cover other functionalities

# Add more test cases as needed