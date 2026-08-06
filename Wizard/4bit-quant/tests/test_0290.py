python
import pytest
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
from src_0290 import task_func

def test_task_func():
    X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = [0, 1, 1]
    n_splits = 2
    batch_size = 32
    epochs = 10

    history = task_func(X, y, n_splits, batch_size, epochs)

    assert len(history) == n_splits
    assert isinstance(history[0], tf.keras.callbacks.History)