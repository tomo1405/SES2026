import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from src_0773 import task_func

def test_task_func_1():
    """
    Test case 1:
    Check if the function returns the expected result for a given input.
    """
    num_samples = 1000
    k = 5
    d = 2
    random_seed = 42
    expected_result = 0.5

    np.random.seed(random_seed)
    data = np.random.randn(num_samples, 1)*k + d
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    mse = task_func(num_samples, k, d, random_seed)

    assert mse == expected_result

def test_task_func_2():
    """
    Test case 2:
    Check if the function returns the expected result for a different input.
    """
    num_samples = 500
    k = 10
    d = 5
    random_seed = None
    expected_result = 2.5

    np.random.seed(random_seed)
    data = np.random.randn(num_samples, 1)*k + d
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    mse = task_func(num_samples, k, d, random_seed)

    assert mse == expected_result

def test_task_func_3():
    """
    Test case 3:
    Check if the function raises an error when the input is invalid.
    """
    num_samples = -1
    k = 5
    d = 2
    random_seed = None

    with pytest.raises(ValueError):
        task_func(num_samples, k, d, random_seed)