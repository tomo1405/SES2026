python
import pandas as pd
import random
import pytest

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):

    distribution = {category: random.randint(*value_range) for category in CATEGORIES}
    df = pd.DataFrame(list(distribution.items()), columns=['Category', 'Count'])

    return df

def test_task_func():
    # Test case 1
    value_range = (0, 100)
    expected_df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D', 'E'], 'Count': [42, 73, 10, 89, 27]})
    assert task_func(value_range).equals(expected_df)

    # Test case 2
    value_range = (50, 150)
    expected_df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D', 'E'], 'Count': [93, 124, 155, 146, 95]})
    assert task_func(value_range).equals(expected_df)

    # Test case 3
    value_range = (100, 200)
    expected_df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D', 'E'], 'Count': [142, 173, 204, 195, 144]})
    assert task_func(value_range).equals(expected_df)