import pytest
from src_0904 import task_func

def test_task_func():
    d = {'x': [1, 2, 3], 'y': [2, 3, 4], 'z': [3, 4, 5]}
    model = task_func(d)
    assert isinstance(model, LinearRegression)
    assert model.coef_.shape[0] == 2
    assert model.coef_.shape[1] == 1