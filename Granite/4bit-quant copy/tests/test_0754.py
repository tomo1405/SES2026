import math
import random
import statistics
from src_0754 import task_func
import pytest

RADIUS = 5

def test_task_func():
    n = 1000  # Number of iterations to test
    distances = []

    for _ in range(n):
        theta = 2 * math.pi * random.random()
        r = RADIUS * math.sqrt(random.random())
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)

    expected_mean = round(statistics.mean(distances), 4)
    actual_mean = task_func(n)
    assert actual_mean == expected_mean, "Expected mean: {}, Actual mean: {}".format(expected_mean, actual_mean)

if __name__ == "__main__":
    pytest.main()