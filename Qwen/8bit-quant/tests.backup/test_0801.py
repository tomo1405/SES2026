import pytest
from src_0801 import task_func, create_test_csv
import os
from collections import Counter

# Constants
CSV_FILE_PATH = 'match_data.csv'

@pytest.fixture(autouse=True)
def cleanup():
    # Remove the CSV file after each test
    if os.path.exists(CSV_FILE_PATH):
        os.remove(CSV_FILE_PATH)

def test_task_func_with_existing_csv():
    # Create a test CSV file
    content = [
        ['team', 'goals', 'penalties'],
        ['Team A', '2', '1'],
        ['Team B', '1', '2'],
        ['Team C', '3', '0']
    ]
    create_test_csv(CSV_FILE_PATH, content)

    # Define goals and penalties
    goals = {'Team D': 4}
    penalties = {'Team D': 1}

    # Expected result
    expected_counts = Counter({'goals': 10, 'penalties': 4})

    # Call the function
    result = task_func(goals, penalties)

    # Assert the result
    assert result == expected_counts

def test_task_func_without_existing_csv():
    # Define goals and penalties
    goals = {'Team A': 5}
    penalties = {'Team A': 3}

    # Expected result
    expected_counts = Counter({'goals': 5, 'penalties': 3})

    # Call the function
    result = task_func(goals, penalties)

    # Assert the result
    assert result == expected_counts

def test_task_func_with_empty_csv():
    # Create an empty test CSV file
    create_test_csv(CSV_FILE_PATH, [])

    # Define goals and penalties
    goals = {'Team E': 6}
    penalties = {'Team E': 2}

    # Expected result
    expected_counts = Counter({'goals': 6, 'penalties': 2})

    # Call the function
    result = task_func(goals, penalties)

    # Assert the result
    assert result == expected_counts

def test_task_func_with_no_teams():
    # Create a test CSV file
    content = [
        ['team', 'goals', 'penalties'],
        ['Team F', '0', '0'],
        ['Team G', '0', '0']
    ]
    create_test_csv(CSV_FILE_PATH, content)

    # Define goals and penalties
    goals = {}
    penalties = {}

    # Expected result
    expected_counts = Counter({'goals': 0, 'penalties': 0})

    # Call the function
    result = task_func(goals, penalties)

    # Assert the result
    assert result == expected_counts