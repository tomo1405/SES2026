import math
import random
import statistics
from src_0754 import task_func

def test_task_func():
    n = 1000
    distances = []

    for _ in range(n):
        theta = 2 * math.pi * random.random()
        r = 5 * math.sqrt(random.random())
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)

    expected_mean = round(statistics.mean(distances), 4)
    actual_mean = task_func(n)
    assert expected_mean == actual_mean, "Incorrect mean calculation"

def test_task_func_with_zero_radius():
    n = 1000
    distances = []

    for _ in range(n):
        theta = 2 * math.pi * random.random()
        r = 0 * math.sqrt(random.random())
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)

    expected_mean = round(statistics.mean(distances), 4)
    actual_mean = task_func(n)
    assert expected_mean == actual_mean, "Incorrect mean calculation"

def test_task_func_with_negative_radius():
    n = 1000
    distances = []

    for _ in range(n):
        theta = 2 * math.pi * random.random()
        r = -5 * math.sqrt(random.random())
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)

    expected_mean = round(statistics.mean(distances), 4)
    actual_mean = task_func(n)
    assert expected_mean == actual_mean, "Incorrect mean calculation"