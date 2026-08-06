import pytest
from src_0290 import task_func

@pytest.mark.parametrize("X, y, n_splits, batch_size, epochs", [
    (X_train, y_train, 5, 32, 10),
    (X_test, y_test, 10, 64, 15),
])
def test_task_func(X, y, n_splits, batch_size, epochs):
    history = task_func(X, y, n_splits, batch_size, epochs)
    assert isinstance(history, list)
    for hist in history:
        assert isinstance(hist, tf.keras.callbacks.History)