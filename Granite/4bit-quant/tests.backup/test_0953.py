import pandas as pd
import random
from datetime import datetime
import pytest

from src_0953 import task_func

@pytest.fixture
def mock_random():
    """
    Mock the random module for testing purposes.
    """
    mock_random = random.Random()
    mock_random.seed(42)
    return mock_random

def test_task_func_with_valid_input(mock_random):
    """
    Test the task_func function with valid input.
    """
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 2
    expected_df = pd.DataFrame({
        "Task Name": ["Task_1", "Task_2"],
        "Assigned To": ["James Brown", "Robert Davis"],
        "Due Date": ["2023-03-14", "2023-03-14"]
    })
    actual_df = task_func(task_list, n_tasks)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_with_invalid_input():
    """
    Test the task_func function with invalid input.
    """
    with pytest.raises(ValueError) as exc_info:
        task_func([], -1)
    assert "n_tasks cannot be negative." in str(exc_info.value)