import pytest
from src_0290 import task_func

def test_task_func():
    X = [[1, 2], [3, 4], [5, 6], [7, 8]]
    y = [0, 1, 0, 1]
    n_splits = 2
    batch_size = 2
    epochs = 1

    history = task_func(X, y, n_splits, batch_size, epochs)

    assert len(history) == n_splits
    assert all(len(hist) == epochs for hist in history)
    assert all(hist.history['accuracy'][0] > 0.5 for hist in history)