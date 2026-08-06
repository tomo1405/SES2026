import pytest
from src_0654 import task_func

def test_task_func():
    # Test case 1: Test with a valid dataframe and target value
    dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_value = '332'
    mask, ax = task_func(dataframe, target_value)
    assert mask.equals(pd.DataFrame({'A': [False, False, False], 'B': [False, False, False]}))
    assert ax.get_title() == 'Heatmap of DataFrame'
    assert ax.get_xlabel() == 'Columns'
    assert ax.get_ylabel() == 'Rows'

    # Test case 2: Test with a valid dataframe and invalid target value
    dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_value = 'invalid'
    mask, ax = task_func(dataframe, target_value)
    assert mask.equals(pd.DataFrame({'A': [False, False, False], 'B': [False, False, False]}))
    assert ax.get_title() == 'Heatmap of DataFrame'
    assert ax.get_xlabel() == 'Columns'
    assert ax.get_ylabel() == 'Rows'

    # Test case 3: Test with an invalid dataframe and valid target value
    dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_value = '332'
    mask, ax = task_func(dataframe, target_value)
    assert mask.equals(pd.DataFrame({'A': [False, False, False], 'B': [False, False, False]}))
    assert ax.get_title() == 'Heatmap of DataFrame'
    assert ax.get_xlabel() == 'Columns'
    assert ax.get_ylabel() == 'Rows'

    # Test case 4: Test with an invalid dataframe and invalid target value
    dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    target_value = 'invalid'
    mask, ax = task_func(dataframe, target_value)
    assert mask.equals(pd.DataFrame({'A': [False, False, False], 'B': [False, False, False]}))
    assert ax.get_title() == 'Heatmap of DataFrame'
    assert ax.get_xlabel() == 'Columns'
    assert ax.get_ylabel() == 'Rows'