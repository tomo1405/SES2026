python
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import pytest

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
    # Test case 1: length=10, range_limit=100, seed=0
    axes, random_numbers = task_func(10, 100, 0)
    assert len(random_numbers) == 10
    assert axes.get_title() == 'Distribution of 10 random numbers'
    assert axes.get_xlabel() == 'Value'
    assert axes.get_ylabel() == 'Frequency'

    # Test case 2: length=5, range_limit=50, seed=1
    axes, random_numbers = task_func(5, 50, 1)
    assert len(random_numbers) == 5
    assert axes.get_title() == 'Distribution of 5 random numbers'
    assert axes.get_xlabel() == 'Value'
    assert axes.get_ylabel() == 'Frequency'

    # Test case 3: length=10, range_limit=1, seed=2
    with pytest.raises(ValueError):
        task_func(10, 1, 2)