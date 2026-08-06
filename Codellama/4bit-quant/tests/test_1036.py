import pytest
from src_1036 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create test data
    feature = pd.Series([1, 2, 3, 4, 5])
    target = pd.Series([0, 1, 0, 1, 0])

    # Call the function and check the output
    cm, ax = task_func(feature, target)
    assert isinstance(cm, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert cm.shape == (2, 2)
    assert ax.get_title() == "Confusion Matrix"
    assert ax.get_xlabel() == "Predicted"
    assert ax.get_ylabel() == "Actual"
    assert ax.get_xticks() == [0, 1]
    assert ax.get_yticks() == [0, 1]
    assert ax.get_xticklabels() == ["No", "Yes"]
    assert ax.get_yticklabels() == ["No", "Yes"]

if __name__ == "__main__":
    pytest.main()