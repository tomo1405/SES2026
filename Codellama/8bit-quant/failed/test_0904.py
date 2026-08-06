import pytest
from src_0904 import task_func

def test_task_func():
    d = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10], 'z': [3, 6, 9, 12, 15]}
    target = 'z'

    model = task_func(d, target)

    assert isinstance(model, LinearRegression)
    assert model.coef_[0] == 1
    assert model.intercept_ == 0