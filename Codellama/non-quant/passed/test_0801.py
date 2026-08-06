import pytest
from src_0801 import task_func

def test_task_func_with_valid_input():
    goals = {'Team A': 2, 'Team B': 1, 'Team C': 3}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 0}
    expected_counts = {'goals': 6, 'penalties': 3}

    counts = task_func(goals, penalties)

    assert counts == expected_counts

def test_task_func_with_invalid_input():
    goals = {'Team A': 2, 'Team B': 1, 'Team C': 3}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 0}
    expected_counts = {'goals': 6, 'penalties': 3}

    counts = task_func(goals, penalties, 'invalid_file_path')

    assert counts == expected_counts

def test_task_func_with_empty_input():
    goals = {}
    penalties = {}
    expected_counts = {'goals': 0, 'penalties': 0}

    counts = task_func(goals, penalties)

    assert counts == expected_counts