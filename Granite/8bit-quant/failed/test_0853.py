import pytest
from src_0853 import task_func

def test_task_func():
    max_length = 10
    n_samples = 5
    seed = 42
    expected_output = ['nqjyzmt', 'hkuoxwrg', 'yvqazvop', 'gakhfxnt', 'jmqolbti']

    random.seed(seed)
    actual_output = task_func(max_length, n_samples, seed)

    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(0, 5, seed=42)