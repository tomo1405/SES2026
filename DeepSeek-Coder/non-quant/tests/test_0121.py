import pytest
from src_0121 import task_func
from datetime import datetime

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert isinstance(result, pd.Series), "The result should be a pandas Series"
    assert len(result) > 0, "The series should not be empty"

    # Test with custom start and end dates
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 1, 10)
    result = task_func(start_date=start_date, end_date=end_date)
    assert len(result) == 10, "The series should have 10 dates"

    # Test with invalid dates
    with pytest.raises(ValueError):
        task_func(start_date="invalid_date")

    # Test with invalid date range
    with pytest.raises(ValueError):
        task_func(start_date=datetime(2020, 1, 2), end_date=datetime(2020, 1, 1))