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
    # Test case 1
    animals = ['cat', 'dog', 'fish']
    mean = 2
    expected_sales = {'cat': 0, 'dog': 0, 'fish': 0}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

    # Test case 2
    animals = ['cat', 'dog', 'fish']
    mean = 5
    expected_sales = {'cat': 1, 'dog': 2, 'fish': 1}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

    # Test case 3
    animals = []
    mean = 2
    expected_sales = {}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

    # Test case 4
    animals = ['cat', 'dog', 'fish']
    mean = 0
    with pytest.raises(ValueError):
        task_func(animals, mean)