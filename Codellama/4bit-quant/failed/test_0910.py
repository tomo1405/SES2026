import pytest
from src_0910 import task_func

def test_task_func():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    categories = ['Category 1', 'Category 2', 'Category 3']
    expected_df = pd.DataFrame({'Letter': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                               'Category': ['Category 1', 'Category 1', 'Category 1', 'Category 2', 'Category 2', 'Category 2', 'Category 3', 'Category 3', 'Category 3']})

    actual_df = task_func(letters, categories)

    assert actual_df.equals(expected_df)