import pytest
from src_1036 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    feature = pd.Series([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    target = pd.Series([0, 0, 1, 1, 0, 0, 1, 1, 0, 0])
    return feature, target

def test_task_func(sample_data):
    feature, target = sample_data
    cm, ax = task_func(feature, target)
    
    # Check that the confusion matrix is of the correct shape
    assert cm.shape == (2, 2), "Confusion matrix should be 2x2"
    
    # Check that the plot axis is of type Axes
    assert isinstance(ax, plt.Axes), "Return value should be a matplotlib Axes object"

    # Check that the plot has the correct title and labels
    assert ax.get_title() == "Confusion Matrix", "Plot should have the title 'Confusion Matrix'"
    assert ax.get_xlabel() == "Predicted", "Plot should have the x-label 'Predicted'"
    assert ax.get_ylabel() == "Actual", "Plot should have the y-label 'Actual'"

    # Check that the tick labels are correct
    assert ax.get_xticklabels() == ["No", "Yes"], "X-tick labels should be ['No', 'Yes']"
    assert ax.get_yticklabels() == ["No", "Yes"], "Y-tick labels should be ['No', 'Yes']"

    # Check that the confusion matrix values are within the expected range
    assert np.all(np.array(cm) >= 0) and np.all(np.array(cm) <= len(target)), "Confusion matrix values should be non-negative and less than or equal to the number of samples"