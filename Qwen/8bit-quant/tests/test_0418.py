import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0418 import task_func


@pytest.fixture
def data():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([0, 1, 1, 0])
    return X, Y

def test_task_func(data):
    X, Y = data
    model, ax = task_func(X, Y)
    
    # Check if the model is an instance of Sequential
    assert isinstance(model, Sequential)
    
    # Check if the plot axis is an instance of Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the model has been trained (history object should have keys)
    history = model.history.history
    assert 'loss' in history
    assert 'val_loss' in history
    
    # Check if the model output is as expected
    predictions = model.predict(X)
    assert predictions.shape == (4, 1)
    assert all(isinstance(pred, float) for pred in predictions.flatten())

# Run the tests
if __name__ == "__main__":
    pytest.main()