from src_0374 import task_func


def test_task_func():
    # Test case 1: Test with plot=True
    params, fitted_values, ax = task_func(l, x_data, plot=True)
    assert isinstance(params, tuple) and len(params) == 2
    assert isinstance(fitted_values, list) and len(fitted_values) == len(x_data)
    assert isinstance(ax, object)
    
    # Test case 2: Test with plot=False
    params, fitted_values = task_func(l, x_data, plot=False)
    assert isinstance(params, tuple) and len(params) == 2
    assert isinstance(fitted_values, list) and len(fitted_values) == len(x_data)