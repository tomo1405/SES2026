from src_0904 import task_func


def test_task_func():
    d = {'x': [1, 2, 3], 'y': [2, 4, 6], 'z': [3, 6, 9]}
    target = 'z'

    model = task_func(d, target)

    assert isinstance(model, LinearRegression)
    assert model.coef_[0] == 1
    assert model.intercept_ == 0