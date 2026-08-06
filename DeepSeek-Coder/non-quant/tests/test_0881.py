import pytest
from src_0881 import task_func
import pandas as pd
from sklearn.cluster import KMeans

# Test cases for the function
def test_task_func():
    # Test with valid data
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })
    labels, model = task_func(data)
    assert isinstance(labels, np.ndarray), "The labels should be a numpy array"
    assert isinstance(model, KMeans), "The model should be a KMeans instance"

    # Test with invalid data
    invalid_data = pd.DataFrame({
        'A': [1, 2, '3', 4],
        'B': [5, '6', 7, 8]
    })
    with pytest.raises(ValueError):
        task_func(invalid_data)