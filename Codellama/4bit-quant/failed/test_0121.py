import pytest
from src_0121 import task_func

def test_task_func():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42

    dates = task_func(start_date, end_date, seed)

    assert isinstance(dates, pd.Series)
    assert len(dates) == (end_date - start_date).days
    assert all(isinstance(date, datetime) for date in dates)
    assert all(date >= start_date and date <= end_date for date in dates)