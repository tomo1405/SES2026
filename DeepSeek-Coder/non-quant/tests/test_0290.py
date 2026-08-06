import pytest
from src_0290 import task_func
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

# Define test cases
def test_task_func():
    # Define test data
    X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = [0, 1, 0]
    n_splits = 2
    batch_size = 2
    epochs = 1

    # Call the function
    result = task_func(X, y, n_splits, batch_size, epochs)

    # Add assertions to validate the output
    assert isinstance(result, list), "The result should be a list"
    assert len(result) == n_splits, "The number of splits should match n_splits"
    assert all(isinstance(hist, tf.keras.callbacks.History) for hist in result), "Each history should be a History object"

# Run the test
if __name__ == "__main__":
    pytest.main()