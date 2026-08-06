import pytest
from src_0070 import task_func
import matplotlib.pyplot as plt
import io
import numpy as np

@pytest.fixture
def mock_random(monkeypatch):
    # Mock random.randint to return a fixed value for consistent results
    def mock_randint(a, b):
        return 60000  # Fixed salary within the range

    monkeypatch.setattr(random, 'randint', mock_randint)

@pytest.fixture
def mock_plt(monkeypatch):
    # Mock matplotlib's savefig to capture the plot without showing it
    mock_savefig = io.BytesIO()
    monkeypatch.setattr(plt, 'savefig', lambda x: mock_savefig)
    return mock_savefig

def test_task_func(mock_random, mock_plt):
    input_dict = {'EMPXX1': 3, 'EMPXX2': 2, 'NOTEMPXX': 1}
    ax = task_func(input_dict)

    # Check if the plot is created with the correct title and labels
    assert ax.get_title() == 'Salary Distribution in EMPXX Department'
    assert ax.get_xlabel() == 'Salary'
    assert ax.get_ylabel() == 'Number of Employees'

    # Check if the histogram data is as expected
    bars = ax.patches
    expected_heights = [3, 2]  # Since we mocked randint to return 60000, all employees have the same salary
    actual_heights = [bar.get_height() for bar in bars]
    assert actual_heights == expected_heights

    # Check if the plot was saved correctly
    mock_plt.seek(0)
    assert len(mock_plt.getvalue()) > 0