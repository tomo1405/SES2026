import pytest
from src_0869 import task_func

def test_task_func():
    n_colors = 5
    rng_seed = 42
    colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
    expected_output = ['Red', 'Yellow', 'Blue', 'Green', 'Purple']

    output = task_func(n_colors, colors, rng_seed)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_default_colors():
    n_colors = 3
    rng_seed = None
    expected_output = ['Red', 'Blue', 'Yellow']

    output = task_func(n_colors, rng_seed=rng_seed)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_input():
    n_colors = 'invalid'
    rng_seed = 42
    colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple']

    with pytest.raises(TypeError):
        task_func(n_colors, colors, rng_seed)