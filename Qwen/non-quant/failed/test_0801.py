import pytest
from src_0801 import task_func, create_test_csv
import os
from collections import Counter

@pytest.fixture(scope='module')
def setup_test_data():
    test_content = [
        ['team', 'goals', 'penalties'],
        ['Team A', '2', '1'],
        ['Team B', '1', '2'],
        ['Team C', '3', '0']
    ]
    test_csv_path = 'test_data/test_case_2.csv'
    create_test_csv(test_csv_path, test_content)
    yield test_csv_path
    os.remove(test_csv_path)

def test_task_func_with_existing_csv(setup_test_data):
    goals = {'Team D': 4}
    penalties = {'Team E': 3}
    expected_counts = Counter({'goals': 10, 'penalties': 6})
    result = task_func(goals, penalties, csv_file_path=setup_test_data)
    assert result == expected_counts

def test_task_func_without_existing_csv():
    goals = {'Team D': 4}
    penalties = {'Team E': 3}
    expected_counts = Counter({'goals': 4, 'penalties': 3})
    result = task_func(goals, penalties, csv_file_path='non_existent.csv')
    assert result == expected_counts

def test_task_func_empty_input():
    goals = {}
    penalties = {}
    expected_counts = Counter({'goals': 0, 'penalties': 0})
    result = task_func(goals, penalties, csv_file_path='non_existent.csv')
    assert result == expected_counts

def test_task_func_with_zero_values(setup_test_data):
    goals = {'Team A': 0, 'Team B': 0}
    penalties = {'Team C': 0}
    expected_counts = Counter({'goals': 6, 'penalties': 3})
    result = task_func(goals, penalties, csv_file_path=setup_test_data)
    assert result == expected_counts