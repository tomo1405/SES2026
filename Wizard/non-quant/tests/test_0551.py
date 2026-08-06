python
import pytest
from src_0551 import task_func

def test_task_func():
    # Test case 1
    menu_items = [['Item1', 'Item2', 'Item3'], ['Item4', 'Item5', 'Item6']]
    expected_df = pd.DataFrame({'Count': [1, 1, 1, 1, 1, 1]}, index=['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6'])
    expected_df.index.name = 'MenuItem'
    assert task_func(menu_items).equals(expected_df)

    # Test case 2
    menu_items = [['Item1', 'Item2', 'Item3'], ['Item1', 'Item2', 'Item3']]
    expected_df = pd.DataFrame({'Count': [2, 2, 2]}, index=['Item1', 'Item2', 'Item3'])
    expected_df.index.name = 'MenuItem'
    assert task_func(menu_items).equals(expected_df)

    # Test case 3
    menu_items = [['Item1', 'Item2', 'Item3'], ['Item1', 'Item2', 'Item3'], ['Item1', 'Item2', 'Item3']]
    expected_df = pd.DataFrame({'Count': [3, 3, 3]}, index=['Item1', 'Item2', 'Item3'])
    expected_df.index.name = 'MenuItem'
    assert task_func(menu_items).equals(expected_df)