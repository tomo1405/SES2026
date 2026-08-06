import pytest
from src_1117 import task_func
import random
import statistics

@pytest.mark.parametrize("dict1, expected_output", [
    ({"EMP$$": 10}, (44.5, 44.5, [44])),
    ({"EMP$$": 10, "DEV$$": 5}, (44.5, 44.5, [44])),
    ({"DEV$$": 5}, (0, 0, [])),
    ({"EMP$$": 10, "DEV$$": 5, "TEST$$": 3}, (44.5, 44.5, [44])),
])
def test_task_func(dict1, expected_output):
    random.seed(42)  # Set random seed for reproducibility
    mean_age, median_age, mode_age = task_func(dict1)
    assert (mean_age, median_age, mode_age) == expected_output