python
import pandas as pd
from datetime import datetime
import holidays

def test_task_func():
    # Test valid input
    business_days = task_func(datetime(2023, 1, 1), datetime(2023, 12, 31), 'US')
    assert len(business_days) == 252

    # Test invalid input
    try:
        task_func(datetime(2023, 1, 1), datetime(2022, 12, 31), 'US')
    except ValueError as e:
        assert str(e) == "start_date must not be after end_date."

    try:
        task_func(datetime(2023, 1, 1), datetime(2023, 12, 31), 'XX')
    except ValueError as e:
        assert str(e) == "Invalid country code: XX"

    try:
        task_func(datetime(2023, 1, 1), datetime(2023, 12, 31), 123)
    except ValueError as e:
        assert str(e) == "Invalid country code: 123"

    try:
        task_func(123, datetime(2023, 12, 31), 'US')
    except ValueError as e:
        assert str(e) == "start_date and end_date must be datetime objects."