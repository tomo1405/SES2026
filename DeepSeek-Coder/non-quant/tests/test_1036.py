import pytest
from src_1036 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Define test cases
def test_task_func():
    # Create a sample dataset
    data = pd.DataFrame({
        "Feature": [1, 2, 3, 4, 5],
        "Target": [0, 0, 1, 1, 1]
    })
    
    # Call the function
    result, _ = task_func(data["Feature"], data["Target"])
    
    # Assertions to check the output
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 2, "The result should contain two elements"
    assert isinstance(result[0], np.ndarray), "The first element should be a numpy array"
    assert isinstance(result[1], plt.Axes), "The second element should be a matplotlib AxesSubplot"

    # Check the confusion matrix
    cm = result[0]
    assert cm.shape == (2, 2), "The confusion matrix should be a 2x2 matrix"
    assert np.array_equal(cm, np.array([[1, 1], [0, 1]]), "The confusion matrix is incorrect"

    # Check the plot
    assert plt.fignum in plt.get_fignums(), "The plot should be displayed"

# Run the test
if __name__ == "__main__":
    pytest.main()