import keras
import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0419 import task_func


@pytest.fixture
def sample_data():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([0, 1, 1, 1])
    return X, Y

def test_task_func(sample_data):
    X, Y = sample_data
    model, ax = task_func(X, Y)
    
    # Check if the model is an instance of keras.Sequential
    assert isinstance(model, keras.Sequential)
    
    # Check if the axes object is an instance of matplotlib.axes.Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the model has been trained (by checking the number of layers)
    assert len(model.layers) == 1
    
    # Check if the AUC score is within a reasonable range (0 to 1)
    fpr, tpr, _ = roc_curve(Y, model.predict(X).ravel())
    auc_score = auc(fpr, tpr)
    assert 0 <= auc_score <= 1

    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'False positive rate'
    assert ax.get_ylabel() == 'True positive rate'
    assert ax.get_title() == 'ROC curve'
    assert 'AUC' in ax.get_legend().get_texts()[0].get_text()

# To run the tests, use the command: pytest -v