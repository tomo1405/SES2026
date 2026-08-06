import pytest
from src_0329 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, dict), "The result should be a dictionary."
    assert len(result) == 5, "The result should contain 5 teams."
    assert all(isinstance(team, str) for team in result), "All team names should be strings."
    assert all(isinstance(points, int) for points in result.values()), "All points should be integers."