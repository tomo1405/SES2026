python
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    distribution = {category: random.randint(*value_range) for category in CATEGORIES}
    df = pd.DataFrame(list(distribution.items()), columns=['Category', 'Count'])
    return df

# Test the function
def test_task_func():
    # Test case 1
    value_range = (0, 100)
    expected_df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D', 'E'], 'Count': [random.randint(0, 100) for _ in range(5)]})
    assert task_func(value_range).equals(expected_df)

    # Test case 2
    value_range = (50, 150)
    expected_df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D', 'E'], 'Count': [random.randint(50, 150) for _ in range(5)]})
    assert task_func(value_range).equals(expected_df)

    # Test case 3
    value_range = (-100, 100)
    expected_df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D', 'E'], 'Count': [random.randint(-100, 100) for _ in range(5)]})
    assert task_func(value_range).equals(expected_df)

# Run the tests
test_task_func()