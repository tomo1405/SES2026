python
import numpy as np
import pandas as pd
import pytest
from sklearn.ensemble import RandomForestClassifier
from src_0980 import task_func

def test_task_func():
    # Test case 1: Test with default parameters
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    target_array = np.array([0, 1, 0])
    clf = task_func(feature_array, target_array)
    assert isinstance(clf, RandomForestClassifier)

    # Test case 2: Test with custom parameters
    feature_names = ["f1", "f2", "f3", "f4", "f5"]
    target_name = "target"
    seed = 42
    clf = task_func(feature_array, target_array, feature_names, target_name, seed)
    assert isinstance(clf, RandomForestClassifier)

    # Test case 3: Test with invalid input type
    with pytest.raises(TypeError):
        feature_array = "not an array"
        target_array = np.array([0, 1, 0])
        clf = task_func(feature_array, target_array)

    # Test case 4: Test with invalid target array shape
    with pytest.raises(ValueError):
        feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
        target_array = np.array([0, 1])
        clf = task_func(feature_array, target_array)