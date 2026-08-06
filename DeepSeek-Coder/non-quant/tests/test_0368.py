import pytest
from src_0368 import task_func
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def test_task_func():
    # Test with valid datetime objects
    activities = [
        datetime(2023, 10, 1),
        datetime(2023, 10, 2),
        datetime(2023, 10, 3),
        datetime(2023, 10, 4),
        datetime(2023, 10, 5),
        datetime(2023, 10, 6),
        datetime(2023, 10, 7),
        datetime(2023, 10, 8)
    ]
    result = task_func(activities)
    assert result is not None

    # Add more tests as needed to cover different scenarios

if __name__ == "__main__":
    pytest.main()