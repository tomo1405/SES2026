import pandas as pd
import pytest
from src_1045 import task_func


@pytest.mark.parametrize(
    "date_str, booking_data, expected_output",
    [
        (
            "2023-01-01",
            {"Room1": "Booked", "Room2": "Available", "Room3": "Not Listed"},
            (
                pd.DataFrame(
                    data=[
                        ["Room1", "Booked"],
                        ["Room2", "Available"],
                        ["Room3", "Not Listed"],
                        ["Room4", "Not Listed"],
                        ["Room5", "Not Listed"]
                    ],
                    columns=["Room", "Booking Status"]
                ),
                # matplotlib.axes._axes.Axes object
            ),
        ),
        (
            "2022-12-31",
            {"Room1": "Booked", "Room2": "Available", "Room3": "Not Listed"},
            (
                pd.DataFrame(
                    data=[
                        ["Room1", "Booked"],
                        ["Room2", "Available"],
                        ["Room3", "Not Listed"],
                        ["Room4", "Not Listed"],
                        ["Room5", "Not Listed"]
                    ],
                    columns=["Room", "Booking Status"]
                ),
                # matplotlib.axes._axes.Axes object
            ),
        ),
    ],
)
def test_task_func(date_str, booking_data, expected_output):
    report_df, ax = task_func(date_str, booking_data)
    assert report_df.equals(expected_output[0])
    # You can also assert the type of ax and the plot's title
    # assert type(ax) == expected_output[1]
    # assert ax.get_title() == "Booking Statuses for " + date_str