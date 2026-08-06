python
import pytest
from src_0551 import task_func

def test_task_func():
    # Test case 1
    menu_items = [['Item1', 'Item2', 'Item3'], ['Item4', 'Item5', 'Item6']]
    expected_df = pd.DataFrame({'MenuItem': ['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6'],
                                'Count': [1, 1, 1, 1, 1, 1]})
    assert task_func(menu_items).equals(expected_df)

    # Test case 2
    menu_items = [['Item1', 'Item2', 'Item3'], ['Item1', 'Item2', 'Item3']]
    expected_df = pd.DataFrame({'MenuItem': ['Item1', 'Item2', 'Item3'],
                                'Count': [2, 2, 2]})
    assert task_func(menu_items).equals(expected_df)

    # Test case 3
    menu_items = [['Item1', 'Item2', 'Item3'], ['Item1', 'Item2', 'Item3'], ['Item1', 'Item2', 'Item3']]
    expected_df = pd.DataFrame({'MenuItem': ['Item1', 'Item2', 'Item3'],
                                'Count': [3, 3, 3]})
    assert task_func(menu_items).equals(expected_df)