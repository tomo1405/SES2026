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
    # Test case 1: empty list of animals
    assert task_func([], 10) == {}

    # Test case 2: mean of 0
    assert task_func(['cat', 'dog', 'fish'], 0) == {'cat': 0, 'dog': 0, 'fish': 0}

    # Test case 3: mean of 1
    assert task_func(['cat', 'dog', 'fish'], 1) == {'cat': 0, 'dog': 0, 'fish': 0}

    # Test case 4: mean of 2
    assert task_func(['cat', 'dog', 'fish'], 2) == {'cat': 1, 'dog': 1, 'fish': 0}

    # Test case 5: mean of 3
    assert task_func(['cat', 'dog', 'fish'], 3) == {'cat': 2, 'dog': 1, 'fish': 0}

    # Test case 6: mean of 4
    assert task_func(['cat', 'dog', 'fish'], 4) == {'cat': 2, 'dog': 2, 'fish': 0}

    # Test case 7: mean of 5
    assert task_func(['cat', 'dog', 'fish'], 5) == {'cat': 3, 'dog': 2, 'fish': 0}

    # Test case 8: mean of 6
    assert task_func(['cat', 'dog', 'fish'], 6) == {'cat': 3, 'dog': 3, 'fish': 0}

    # Test case 9: mean of 7
    assert task_func(['cat', 'dog', 'fish'], 7) == {'cat': 4, 'dog': 3, 'fish': 0}

    # Test case 10: mean of 8
    assert task_func(['cat', 'dog', 'fish'], 8) == {'cat': 4, 'dog': 4, 'fish': 0}

    # Test case 11: mean of 9
    assert task_func(['cat', 'dog', 'fish'], 9) == {'cat': 5, 'dog': 4, 'fish': 0}

    # Test case 12: mean of 10
    assert task_func(['cat', 'dog', 'fish'], 10) == {'cat': 5, 'dog': 5, 'fish': 0}