import pytest
from src_0419 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    # Generate some sample data for testing
    np.random.seed(0)
    X = np.random.rand(100, 2)
    Y = (X[:, 0] + X[:, 1] > 1).astype(int)
    return X, Y

def test_task_func(sample_data):
    X, Y = sample_data
    model, ax = task_func(X, Y)

    # Check if the model is an instance of keras.models.Sequential
    assert isinstance(model, keras.models.Sequential)

    # Check if the axes object is an instance of matplotlib.axes.Axes
    assert isinstance(ax, plt.Axes)

    # Check if the AUC score is calculated correctly
    Y_pred = model.predict(X, verbose=0).ravel()
    fpr, tpr, _ = roc_curve(Y, Y_pred)
    auc_score = auc(fpr, tpr)
    assert isinstance(auc_score, float)
    assert 0 <= auc_score <= 1

    # Check if the plot has the correct elements
    lines = ax.get_lines()
    assert len(lines) == 2  # One line for the ROC curve and one for the diagonal
    assert lines[0].get_label() == 'AUC = {:.3f}'.format(auc_score)
    assert lines[1].get_linestyle() == '--'  # Diagonal line should be dashed

    # Close the plot to avoid displaying it during tests
    plt.close(fig)