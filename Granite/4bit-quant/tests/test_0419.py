import pytest
from src_0419 import task_func


@pytest.mark.parametrize("X, Y, expected_output", [
    (X_train, Y_train, expected_model_output),
    (X_test, Y_test, expected_ax_output),
    # Add more test cases as needed
])
def test_task_func(X, Y, expected_output):
    model, ax = task_func(X, Y)
    assert model == expected_output[0]
    assert ax == expected_output[1]