import numpy as np
import pytest
import tensorflow as tf
from src_0290 import task_func


@pytest.fixture
def sample_data():
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    return X, y

def test_task_func(sample_data):
    X, y = sample_data
    n_splits = 3
    batch_size = 10
    epochs = 5

    history = task_func(X, y, n_splits, batch_size, epochs)

    assert len(history) == n_splits, "The number of histories should match the number of splits"
    for hist in history:
        assert isinstance(hist, tf.keras.callbacks.History), "Each history should be an instance of tf.keras.callbacks.History"
        assert 'loss' in hist.history, "History should contain 'loss' key"
        assert 'val_loss' in hist.history, "History should contain 'val_loss' key"
        assert 'accuracy' in hist.history, "History should contain 'accuracy' key"
        assert 'val_accuracy' in hist.history, "History should contain 'val_accuracy' key"

def test_task_func_with_invalid_n_splits(sample_data):
    X, y = sample_data
    n_splits = -1
    batch_size = 10
    epochs = 5

    with pytest.raises(ValueError):
        task_func(X, y, n_splits, batch_size, epochs)

def test_task_func_with_zero_epochs(sample_data):
    X, y = sample_data
    n_splits = 3
    batch_size = 10
    epochs = 0

    history = task_func(X, y, n_splits, batch_size, epochs)

    assert len(history) == n_splits, "The number of histories should match the number of splits"
    for hist in history:
        assert isinstance(hist, tf.keras.callbacks.History), "Each history should be an instance of tf.keras.callbacks.History"
        assert 'loss' in hist.history, "History should contain 'loss' key"
        assert 'val_loss' in hist.history, "History should contain 'val_loss' key"
        assert 'accuracy' in hist.history, "History should contain 'accuracy' key"
        assert 'val_accuracy' in hist.history, "History should contain 'val_accuracy' key"