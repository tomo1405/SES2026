import pytest
from src_0150 import task_func

def test_task_func():
    elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
    include_index = False
    expected_df = pd.DataFrame({'Element': elements, 'Count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    actual_df = task_func(elements, include_index)
    assert actual_df.equals(expected_df)

def test_task_func_with_index():
    elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
    include_index = True
    expected_df = pd.DataFrame({'Index': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'Element': elements, 'Count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    actual_df = task_func(elements, include_index)
    assert actual_df.equals(expected_df)

def test_task_func_with_invalid_input():
    elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
    include_index = 'invalid'
    with pytest.raises(ValueError):
        task_func(elements, include_index)