import pytest
from src_1036 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    feature = pd.Series([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    target = pd.Series([0, 0, 1, 1, 0, 1, 0, 1, 0, 1])
    return feature, target

def test_task_func(sample_data):
    feature, target = sample_data
    cm, ax = task_func(feature, target)

    # Check if the confusion matrix is of the correct shape
    assert cm.shape == (2, 2), "Confusion matrix should be a 2x2 array"

    # Check if the plot axis is not None
    assert ax is not None, "Plot axis should not be None"

    # Check if the plot title is set correctly
    assert ax.get_title() == "Confusion Matrix", "Plot title should be 'Confusion Matrix'"

    # Check if the plot x and y labels are set correctly
    assert ax.get_xlabel() == "Predicted", "X label should be 'Predicted'"
    assert ax.get_ylabel() == "Actual", "Y label should be 'Actual'"

    # Check if the tick labels are set correctly
    assert ax.get_xticklabels() == ["No", "Yes"], "X tick labels should be ['No', 'Yes']"
    assert ax.get_yticklabels() == ["No", "Yes"], "Y tick labels should be ['No', 'Yes']"

    # Close the plot to avoid displaying it during testing
    plt.close(ax.figure)