import pytest
from src_0290 import task_func

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6]]
    y = [0, 1, 0]
    n_splits = 2
    batch_size = 32
    epochs = 10

    history = task_func(X, y, n_splits, batch_size, epochs)

    assert len(history) == n_splits
    assert all(isinstance(hist, tf.keras.callbacks.History) for hist in history)
    assert all(hist.history['accuracy'][0] > 0.5 for hist in history)