import io
import random
import sys

import matplotlib.pyplot as plt
import pytest
from src_1048 import task_func


@pytest.fixture
def mock_date_str():
    return "2023-10-05"

@pytest.fixture
def mock_random_values():
    return [42, 77, 12, 88, 56, 34, 91]

def test_task_func(mock_date_str, mock_random_values, monkeypatch):
    # Mock the random.randint function to return specific values
    def mock_randint(a, b):
        return mock_random_values.pop(0)

    monkeypatch.setattr(random, 'randint', mock_randint)

    # Redirect stdout to capture any print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    ax = task_func(mock_date_str)

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Check if the correct number of random values were generated
    assert len(ax.lines[0].get_ydata()) == 5

    # Check if the plot was created correctly
    assert isinstance(ax, plt.Axes)

    # Check if the plot contains the correct data
    assert all(ax.lines[0].get_ydata() == mock_random_values)