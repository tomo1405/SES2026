import pytest
from src_1046 import task_func
from datetime import datetime
from dateutil.parser import parse

# Mocking datetime.now to control the current date in tests
class MockDatetime:
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.datetime = datetime(year, month, day, hour, minute, second)

    def now(self):
        return self.datetime

@pytest.fixture
def mock_datetime(monkeypatch):
    def mock_now():
        return datetime(2023, 1, 1)  # Default mock date
    monkeypatch.setattr(datetime, 'now', mock_now)

def test_task_func_same_year(mock_datetime):
    assert task_func("2023-01-01") == 0

def test_task_func_one_day_before(mock_datetime):
    assert task_func("2022-12-31") == 86400

def test_task_func_one_leap_second_added(mock_datetime):
    # 2020 was a leap year and had a leap second added
    assert task_func("2019-12-31") == 86401

def test_task_func_multiple_leap_seconds(mock_datetime):
    # 2016, 2012, 2009, 2006, 1999, 1997, 1994, 1993, 1990, 1988, 1985, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972
    assert task_func("1970-01-01") == 16 * 86400 + 24  # 16 years with 1 leap second each + 24 leap seconds before 1972

def test_task_func_future_date(mock_datetime):
    assert task_func("2024-01-01") < 0

def test_task_func_invalid_date():
    with pytest.raises(ValueError):
        task_func("invalid-date")