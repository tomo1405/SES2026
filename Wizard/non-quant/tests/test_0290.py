python
import pytest
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
from src_0290 import task_func

def test_task_func():
    X = tf.random.uniform((100, 5))
    y = tf.random.uniform((100,))
    n_splits = 5
    batch_size = 32
    epochs = 10
    
    history = task_func(X, y, n_splits, batch_size, epochs)
    
    assert len(history) == n_splits
    assert all(isinstance(hist, tf.keras.callbacks.History) for hist in history)