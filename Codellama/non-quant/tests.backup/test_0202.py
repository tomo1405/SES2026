import pytest
from src_0202 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column = 'A'
    value = 3

    with pytest.raises(ValueError):
        task_func(df, 'C', value)

    with pytest.raises(ValueError):
        task_func(df, column, 'hello')

    greater_avg, num_greater_value, ax = task_func(df, column, value)
    assert greater_avg == [4, 5]
    assert num_greater_value == 2
    assert ax.shape == (10,)