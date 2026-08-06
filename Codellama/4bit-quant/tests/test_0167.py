from datetime import datetime

import pytest
from src_0167 import task_func


def test_task_func():
    # Test that start_date and end_date must be datetime objects
    with pytest.raises(ValueError):
        task_func(start_date=1, end_date=2)

    # Test that start_date must not be after end_date
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 1, 1))

    # Test that country must be a string
    with pytest.raises(TypeError):
        task_func(country=1)

    # Test that the function returns a list of business days
    assert isinstance(task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'), list)

    # Test that the function returns the correct number of business days
    assert len(task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US')) == 252