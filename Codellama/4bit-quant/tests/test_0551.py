import pandas as pd
from src_0551 import task_func


def test_task_func():
    # Test case 1: Empty list
    assert task_func([]) == pd.DataFrame()

    # Test case 2: Single element list
    assert task_func([['item1']]) == pd.DataFrame({'Count': 1}, index=['item1'])

    # Test case 3: Multiple elements list
    assert task_func([['item1', 'item2'], ['item3', 'item4']]) == pd.DataFrame({'Count': [2, 2]}, index=['item1', 'item2'])

    # Test case 4: Nested list
    assert task_func([['item1', ['item2', 'item3']]]) == pd.DataFrame({'Count': [2]}, index=['item1'])

    # Test case 5: List with duplicates
    assert task_func([['item1', 'item2'], ['item3', 'item4'], ['item1', 'item2']]) == pd.DataFrame({'Count': [3, 2]}, index=['item1', 'item2'])