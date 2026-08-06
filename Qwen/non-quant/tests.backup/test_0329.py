import pytest
from src_0329 import task_func
import collections
import random

def test_task_func_default_teams():
    result = task_func()
    assert len(result) == 5
    assert all(isinstance(team, str) for team in result.keys())
    assert all(isinstance(points, int) for points in result.values())

def test_task_func_custom_teams():
    result = task_func(number_teams=3)
    assert len(result) == 3
    assert all(isinstance(team, str) for team in result.keys())
    assert all(isinstance(points, int) for points in result.values())

def test_task_func_team_names():
    result = task_func()
    expected_teams = {"Team 1", "Team 2", "Team 3", "Team 4", "Team 5"}
    assert set(result.keys()) == expected_teams

def test_task_func_points_distribution():
    result = task_func()
    points = list(result.values())
    assert sorted(points, reverse=True) == [50, 40, 30, 20, 10]

def test_task_func_randomness():
    result1 = task_func()
    result2 = task_func()
    assert result1 != result2, "The results should be different due to randomness"

def test_task_func_ordered_dict():
    result = task_func()
    assert isinstance(result, collections.OrderedDict)

def test_task_func_priority_queue():
    result = task_func()
    points = list(result.values())
    assert points == sorted(points, reverse=True), "The points should be sorted in descending order"