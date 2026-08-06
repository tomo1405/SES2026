import pytest
from src_0492 import task_func
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io
import os

# Mocking the datetime and random modules to control their behavior during testing
class MockDatetime(datetime):
    @classmethod
    def utcnow(cls):
        return cls(2023, 1, 1)

    @classmethod
    def utcfromtimestamp(cls, timestamp):
        return cls(2022, 12, 1)

class MockRandom:
    @staticmethod
    def seed(seed):
        pass

    @staticmethod
    def randint(a, b):
        return 30  # Fixed value for testing

@pytest.fixture
def mock_datetime(monkeypatch):
    monkeypatch.setattr('src_0492.datetime', MockDatetime)

@pytest.fixture
def mock_random(monkeypatch):
    monkeypatch.setattr('src_0492.random', MockRandom)

def test_task_func_negative_epoch(mock_datetime, mock_random):
    with pytest.raises(ValueError) as exc_info:
        task_func(-1000)
    assert str(exc_info.value) == "Start time cannot be negative."

def test_task_func_future_start(mock_datetime, mock_random):
    with pytest.raises(ValueError) as exc_info:
        task_func((MockDatetime.utcnow() + timedelta(days=1)).timestamp() * 1000)
    assert str(exc_info.value) == "Start date must be before current time."

def test_task_func_valid_input(mock_datetime, mock_random):
    sales_data, ax = task_func(MockDatetime.utcfromtimestamp(0).timestamp() * 1000)
    expected_categories = ["Electronics", "Clothing", "Home", "Books", "Sports"]
    assert list(sales_data.keys()) == expected_categories
    for sales in sales_data.values():
        assert len(sales) == 365  # 365 days between January 1, 2022 and January 1, 2023
        assert all(sale == 30 for sale in sales)  # All sales should be 30 due to MockRandom

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Days since 2022-12-01 00:00:00"
    assert ax.get_ylabel() == "Sales"
    assert ax.get_legend().get_texts()[0].get_text() == "Electronics"

def test_task_func_with_seed(mock_datetime, mock_random):
    sales_data_1, _ = task_func(MockDatetime.utcfromtimestamp(0).timestamp() * 1000, seed=42)
    sales_data_2, _ = task_func(MockDatetime.utcfromtimestamp(0).timestamp() * 1000, seed=42)
    assert sales_data_1 == sales_data_2

def test_task_func_without_seed(mock_datetime, mock_random):
    sales_data_1, _ = task_func(MockDatetime.utcfromtimestamp(0).timestamp() * 1000)
    sales_data_2, _ = task_func(MockDatetime.utcfromtimestamp(0).timestamp() * 1000)
    assert sales_data_1 != sales_data_2