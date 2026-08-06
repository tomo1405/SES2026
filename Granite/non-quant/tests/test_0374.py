import pytest
from src_0374 import task_func

def test_task_func():
    l = [1, 2, 3, 4, 5]
    x_data = [1, 2, 3, 4, 5]
    params, fitted_values = task_func(l, x_data)
    assert len(params) == 2
    assert len(fitted_values) == 5
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert len(params) == 2
    assert len(fitted_values) == 5
    assert ax.get_xlabel() == 'x_data'
    assert ax.get_ylabel() == 'l'

if __name__ == "__main__":
    pytest.main()