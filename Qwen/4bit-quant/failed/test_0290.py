import pytest
from src_0290 import task_func
import numpy as np

@pytest.fixture
def sample_data():
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 0, 1])
    return X, y

def test_task_func(sample_data):
    X, y = sample_data
    n_splits = 2
    batch_size = 2
    epochs = 2

    history = task_func(X, y, n_splits, batch_size, epochs)
    
    assert len(history) == n_splits, "The number of splits should match the number of histories returned."
    for hist in history:
        assert isinstance(hist, tf.keras.callbacks.History), "Each history should be an instance of tf.keras.callbacks.History."
        assert 'loss' in hist.history, "History should contain 'loss' key."
        assert 'val_loss' in hist.history, "History should contain 'val_loss' key."
        assert 'accuracy' in hist.history, "History should contain 'accuracy' key."
        assert 'val_accuracy' in hist.history, "History should contain 'val_accuracy' key."

def test_task_func_with_different_n_splits(sample_data):
    X, y = sample_data
    n_splits = 4
    batch_size = 2
    epochs = 2

    history = task_func(X, y, n_splits, batch_size, epochs)
    
    assert len(history) == n_splits, "The number of splits should match the number of histories returned."
    for hist in history:
        assert isinstance(hist, tf.keras.callbacks.History), "Each history should be an instance of tf.keras.callbacks.History."
        assert 'loss' in hist.history, "History should contain 'loss' key."
        assert 'val_loss' in hist.history, "History should contain 'val_loss' key."
        assert 'accuracy' in hist.history, "History should contain 'accuracy' key."
        assert 'val_accuracy' in hist.history, "History should contain 'val_accuracy' key."

def test_task_func_with_invalid_n_splits(sample_data):
    X, y = sample_data
    n_splits = 1
    batch_size = 2
    epochs = 2

    with pytest.raises(ValueError) as excinfo:
        task_func(X, y, n_splits, batch_size, epochs)
    assert "n_splits must be at least 2" in str(excinfo.value)

def test_task_func_with_zero_epochs(sample_data):
    X, y = sample_data
    n_splits = 2
    batch_size = 2
    epochs = 0

    with pytest.raises(ValueError) as excinfo:
        task_func(X, y, n_splits, batch_size, epochs)
    assert "epochs must be at least 1" in str(excinfo.value)