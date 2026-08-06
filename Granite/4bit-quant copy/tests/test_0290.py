import pytest
from src_0290 import task_func

@pytest.mark.parametrize("X, y, n_splits, batch_size, epochs, expected_output", [
    (X_train, y_train, 5, 32, 10, history),
    (X_test, y_test, 10, 64, 20, history),
])
def test_task_func(X, y, n_splits, batch_size, epochs, expected_output):
    result = task_func(X, y, n_splits, batch_size, epochs)
    assert result == expected_output