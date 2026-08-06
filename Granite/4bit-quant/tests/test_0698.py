import pytest
from src_0698 import task_func

def test_task_func():
    df = {'feature': [1, 2, 3, 4, 5], 'value': [2, 4, 6, 8, 10]}
    expected_output = {'coefficients': [1.4], 'intercept': [1.4]}
    output = task_func(df)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func('invalid input')