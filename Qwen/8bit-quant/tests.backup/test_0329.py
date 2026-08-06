import pytest
from src_0329 import task_func
import random

def test_task_func_default_teams():
    result = task_func()
    assert len(result) == 5
    assert all(isinstance(team, str) and team.startswith("Team ") for team in result.keys())
    assert all(isinstance(points, int) for points in result.values())

def test_task_func_custom_teams():
    result = task_func(number_teams=3)
    assert len(result) == 3
    assert all(isinstance(team, str) and team.startswith("Team ") for team in result.keys())
    assert all(isinstance(points, int) for points in result.values())

def test_task_func_points_distribution():
    result = task_func()
    points = list(result.values())
    assert sorted(points, reverse=True) == points

def test_task_func_randomness():
    random.seed(0)
    result1 = task_func()
    random.seed(0)
    result2 = task_func()
    assert result1 == result2

def test_task_func_unique_teams():
    result = task_func()
    assert len(result) == len(set(result.keys()))