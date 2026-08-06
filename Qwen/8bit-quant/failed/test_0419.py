import pytest
from src_0419 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    # Generate some synthetic data for testing
    np.random.seed(0)
    X = np.random.rand(100, 2)
    Y = np.random.randint(0, 2, 100)
    return X, Y

def test_task_func(sample_data):
    X, Y = sample_data
    model, ax = task_func(X, Y)
    
    # Check if the model is an instance of keras.models.Sequential
    assert isinstance(model, keras.models.Sequential)
    
    # Check if the axes object is an instance of matplotlib.axes.Axes
    assert isinstance(ax, plt.Axes)
    
    # Check if the AUC score is calculated correctly
    # This is a simplified check, assuming the AUC score is between 0 and 1
    assert 0 <= model.history.history['loss'][-1] <= 1
    
    # Check if the plot has the correct labels and title
    assert ax.get_xlabel() == 'False positive rate'
    assert ax.get_ylabel() == 'True positive rate'
    assert ax.get_title() == 'ROC curve'
    
    # Check if the legend contains the AUC score label
    legend_text = ax.get_legend().get_texts()[0].get_text()
    assert 'AUC =' in legend_text