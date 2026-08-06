import random

import matplotlib
import pytest
from src_0201 import task_func


# Mocking the random and matplotlib modules to avoid side effects in tests
class MockRandom:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def random(self):
        if self.index >= len(self.values):
            raise IndexError("No more values to mock")
        value = self.values[self.index]
        self.index += 1
        return value

class MockMatplotlib:
    def plot(self, *args, **kwargs):
        pass

    def show(self):
        pass

@pytest.fixture
def mock_random(monkeypatch):
    mock_values = [0.1, 0.3, 0.5, 0.7, 0.9]  # Example values for testing
    monkeypatch.setattr(random, 'random', MockRandom(mock_values).random)

@pytest.fixture
def mock_matplotlib(monkeypatch):
    monkeypatch.setattr(matplotlib.pyplot, 'plot', MockMatplotlib().plot)
    monkeypatch.setattr(matplotlib.pyplot, 'show', MockMatplotlib().show)

def test_task_func_with_positive_n(mock_random, mock_matplotlib):
    n = 5
    value = 0.5
    result = task_func(n, value)
    expected_greater_avg = [0.7, 0.9]
    expected_num_greater_value = 2
    assert result == (expected_greater_avg, expected_num_greater_value)

def test_task_func_with_zero_n():
    n = 0
    value = 0.5
    result = task_func(n, value)
    assert result == ([], 0)

def test_task_func_with_negative_n():
    n = -1
    value = 0.5
    result = task_func(n, value)
    assert result == ([], 0)

def test_task_func_with_all_numbers_less_than_value(mock_random, mock_matplotlib):
    n = 5
    value = 1.0
    result = task_func(n, value)
    expected_greater_avg = []
    expected_num_greater_value = 0
    assert result == (expected_greater_avg, expected_num_greater_value)

def test_task_func_with_all_numbers_greater_than_value(mock_random, mock_matplotlib):
    n = 5
    value = -1.0
    result = task_func(n, value)
    expected_greater_avg = [0.1, 0.3, 0.5, 0.7, 0.9]
    expected_num_greater_value = 5
    assert result == (expected_greater_avg, expected_num_greater_value)