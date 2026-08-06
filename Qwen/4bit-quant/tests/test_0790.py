from src_0790 import task_func


def test_task_func_output_shape():
    result = task_func()
    assert result.shape == (ARRAY_LENGTH, 1), "The output should be a 2D array with shape (10, 1)"

def test_task_func_min_max_values():
    result = task_func()
    min_value = result.min()
    max_value = result.max()
    assert min_value >= 0 and max_value <= 1, "The values should be scaled between 0 and 1"

def test_task_func_reproducibility():
    first_run = task_func()
    second_run = task_func()
    assert np.array_equal(first_run, second_run), "Multiple runs should produce the same result due to fixed seed"