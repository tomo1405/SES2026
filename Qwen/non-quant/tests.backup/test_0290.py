import pytest
from src_0290 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    return X, y

def test_task_func(sample_data):
    X, y = sample_data
    n_splits = 5
    batch_size = 32
    epochs = 10

    history = task_func(X, y, n_splits, batch_size, epochs)

    assert len(history) == n_splits, "The number of splits should match the number of histories"
    for hist in history:
        assert isinstance(hist, tf.keras.callbacks.History), "Each history should be an instance of tf.keras.callbacks.History"
        assert 'loss' in hist.history, "History should contain 'loss'"
        assert 'val_loss' in hist.history, "History should contain 'val_loss'"
        assert 'accuracy' in hist.history, "History should contain 'accuracy'"
        assert 'val_accuracy' in hist.history, "History should contain 'val_accuracy'"

def test_task_func_invalid_n_splits(sample_data):
    X, y = sample_data
    n_splits = -1
    batch_size = 32
    epochs = 10

    with pytest.raises(ValueError):
        task_func(X, y, n_splits, batch_size, epochs)

def test_task_func_invalid_batch_size(sample_data):
    X, y = sample_data
    n_splits = 5
    batch_size = 0
    epochs = 10

    with pytest.raises(ValueError):
        task_func(X, y, n_splits, batch_size, epochs)

def test_task_func_invalid_epochs(sample_data):
    X, y = sample_data
    n_splits = 5
    batch_size = 32
    epochs = -1

    with pytest.raises(ValueError):
        task_func(X, y, n_splits, batch_size, epochs)