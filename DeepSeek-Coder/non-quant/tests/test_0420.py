import pytest
from src_0420 import task_func
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample dataset for testing
    X = [[0], [1], [2], [3], [4]]
    Y = [0, 1, 0, 1, 1]

    # Call the function
    model, ax = task_func(X, Y)

    # Add assertions to verify the output
    assert isinstance(model, keras.engine.sequential.Sequential), "The model should be a Sequential model"
    assert isinstance(ax, plt.Axes), "The ax should be a matplotlib Axes object"
    assert ax.get_xlabel() == 'Recall', "The x-axis label should be 'Recall'"
    assert ax.get_ylabel() == 'Precision', "The y-axis label should be 'Precision'"
    assert ax.get_title() == 'Precision-Recall Curve', "The title should be 'Precision-Recall Curve'"