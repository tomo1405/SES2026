import numpy as np
from sklearn.preprocessing import MinMaxScaler
from src_0790 import task_func


def test_task_func_output_shape():
    result = task_func()
    assert result.shape == (ARRAY_LENGTH, 1), "The output shape should be (10, 1)"

def test_task_func_min_max_values():
    result = task_func()
    assert np.min(result) == 0, "The minimum value of the scaled array should be 0"
    assert np.max(result) == 1, "The maximum value of the scaled array should be 1"

def test_task_func_reproducibility():
    result1 = task_func()
    result2 = task_func()
    assert np.array_equal(result1, result2), "The function should produce the same output on multiple calls due to the fixed seed"

def test_task_func_random_state():
    np.random.seed(42)
    array = np.random.randint(0, 10, ARRAY_LENGTH).reshape(-1, 1)
    scaler = MinMaxScaler()
    expected_result = scaler.fit_transform(array)
    
    actual_result = task_func()
    assert np.array_equal(actual_result, expected_result), "The function's output does not match the expected result with the given random state"