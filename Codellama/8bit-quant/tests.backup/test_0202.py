import pytest
from src_0202 import task_func

def test_task_func_column_not_in_df():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df, 'c', 1)

def test_task_func_value_not_number():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df, 'a', '1')

def test_task_func_valid_input():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    greater_avg, num_greater_value, ax = task_func(df, 'a', 2)
    assert greater_avg == [3]
    assert num_greater_value == 1
    assert ax.shape == (10,)