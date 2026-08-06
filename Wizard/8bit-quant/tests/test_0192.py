python
import random
import pytest
from scipy import stats

def task_func(animals, mean):
    if not animals:
        return {}

    sales = {animal: 0 for animal in animals}
    num_customers = stats.poisson(mu=mean).rvs()

    for _ in range(num_customers):
        animal = random.choice(animals)
        sales[animal] += 1
    return sales

def test_task_func():
    # Test case 1: Empty list of animals
    assert task_func([], 10) == {}

    # Test case 2: Mean of 0
    assert task_func(['cat', 'dog', 'fish'], 0) == {'cat': 0, 'dog': 0, 'fish': 0}

    # Test case 3: Mean of 10
    sales = task_func(['cat', 'dog', 'fish'], 10)
    assert len(sales) == 3
    assert all(isinstance(sales[animal], int) for animal in sales)
    assert all(sales[animal] >= 0 for animal in sales)
    assert all(sales[animal] <= 10 for animal in sales)