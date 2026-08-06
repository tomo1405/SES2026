import pytest
from src_0329 import task_func

def test_task_func_default():
    result = task_func()
    assert len(result) == 5
    assert all(isinstance(team, str) for team in result.keys())
    assert all(isinstance(points, int) for points in result.values())

def test_task_func_custom_number_of_teams():
    result = task_func(3)
    assert len(result) == 3
    assert all(isinstance(team, str) for team in result.keys())
    assert all(isinstance(points, int) for points in result.values())

def test_task_func_points_distribution():
    result = task_func()
    points = list(result.values())
    assert len(set(points)) == 5  # Ensure all teams have different points
    assert min(points) == 10 and max(points) == 50

def test_task_func_sorted_by_points_desc():
    result = task_func()
    previous_points = float('inf')
    for points in result.values():
        assert points <= previous_points
        previous_points = points

def test_task_func_reproducibility():
    random.seed(0)
    first_run = task_func()
    random.seed(0)
    second_run = task_func()
    assert first_run == second_run

def test_task_func_team_names():
    result = task_func()
    expected_teams = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5"]
    assert set(result.keys()) == set(expected_teams)