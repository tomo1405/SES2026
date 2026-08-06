python
import pytest
from src_0654 import task_func

def test_task_func():
    # Test case 1: Valid input
    dataframe = {'A': ['111', '222', '333', '444'], 'B': ['111', '222', '332', '444'], 'C': ['111', '222', '333', '444']}
    dataframe = pd.DataFrame(dataframe)
    target_value = '332'
    expected_mask = pd.DataFrame({'A': [False, False, True, False], 'B': [False, False, True, False], 'C': [False, False, True, False]})
    expected_ax = None

    mask, ax = task_func(dataframe, target_value)

    assert mask.equals(expected_mask)
    assert ax == expected_ax

    # Test case 2: Invalid input (target value not present in dataframe)
    dataframe = {'A': ['111', '222', '333', '444'], 'B': ['111', '222', '333', '444'], 'C': ['111', '222', '333', '444']}
    dataframe = pd.DataFrame(dataframe)
    target_value = '332'
    expected_mask = pd.DataFrame({'A': [False, False, False, False], 'B': [False, False, False, False], 'C': [False, False, False, False]})
    expected_ax = None

    mask, ax = task_func(dataframe, target_value)

    assert mask.equals(expected_mask)
    assert ax == expected_ax

    # Test case 3: Invalid input (empty dataframe)
    dataframe = {'A': [], 'B': [], 'C': []}
    dataframe = pd.DataFrame(dataframe)
    target_value = '332'
    expected_mask = pd.DataFrame({'A': [], 'B': [], 'C': []})
    expected_ax = None

    mask, ax = task_func(dataframe, target_value)

    assert mask.equals(expected_mask)
    assert ax == expected_ax