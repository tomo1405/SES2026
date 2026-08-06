import pytest
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def task_func(length, range_limit=100, seed=0):
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1")

    random.seed(seed)
    np.random.seed(seed)

    random_numbers = [random.randint(1, range_limit) for _ in range(length)]
    random_numbers.sort()

    # Initialize a fresh plot
    plt.figure()
    plot = sns.histplot(random_numbers, kde=False)

    return plot.axes, random_numbers

def test_task_func():
    length = 10
    range_limit = 100
    seed = 0
    expected_output = ([<AxesSubplot:>], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54])

    actual_output = task_func(length, range_limit, seed)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_invalid_range_limit():
    with pytest.raises(ValueError) as excinfo:
        task_func(10, 1)
    assert "range_limit must be greater than 1" in str(excinfo.value)