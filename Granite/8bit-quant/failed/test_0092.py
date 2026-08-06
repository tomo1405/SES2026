import pytest
from src_0092 import task_func

def test_task_func():
    data = ...  # provide sample input data
    column1 = ...  # provide sample column1 name
    column2 = ...  # provide sample column2 name
    expected_slope = ...  # provide expected slope value
    expected_intercept = ...  # provide expected intercept value
    expected_r_value = ...  # provide expected r_value value
    expected_p_value = ...  # provide expected p_value value
    expected_std_err = ...  # provide expected std_err value
    expected_ax = ...  # provide expected ax value

    slope, intercept, r_value, p_value, std_err, ax = task_func(data, column1, column2)

    assert slope == expected_slope
    assert intercept == expected_intercept
    assert r_value == expected_r_value
    assert p_value == expected_p_value
    assert std_err == expected_std_err
    assert ax == expected_ax