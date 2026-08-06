import pytest
from src_0278 import task_func

def test_task_func():
    n = 10
    points = [(random.random(), random.random()) for i in range(n)]
    closest_pair = min(combinations(points, 2), key=lambda pair: math.hypot(pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]))
    expected_result = closest_pair
    actual_result = task_func(n)
    assert actual_result == expected_result, "Task function returned an incorrect result"

def test_task_func_with_invalid_input():
    n = -1
    expected_result = None
    actual_result = task_func(n)
    assert actual_result == expected_result, "Task function did not handle invalid input correctly"