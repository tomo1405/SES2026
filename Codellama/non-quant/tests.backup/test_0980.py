import pytest
from src_0980 import task_func
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def test_task_func():
    # Test case 1: Test that the function returns a RandomForestClassifier object
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    clf = task_func(feature_array, target_array)
    assert isinstance(clf, RandomForestClassifier)

    # Test case 2: Test that the function returns a RandomForestClassifier object with the correct parameters
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    clf = task_func(feature_array, target_array, feature_names=["f1", "f2", "f3", "f4", "f5"], target_name="target", seed=42)
    assert isinstance(clf, RandomForestClassifier)
    assert clf.n_estimators == 100
    assert clf.max_depth == 5
    assert clf.min_samples_split == 2
    assert clf.min_samples_leaf == 1
    assert clf.max_features == "auto"
    assert clf.bootstrap == True
    assert clf.oob_score == False
    assert clf.n_jobs == -1
    assert clf.random_state == 42

    # Test case 3: Test that the function raises a ValueError when the input arrays are not of the same length
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1, 0])
    with pytest.raises(ValueError):
        task_func(feature_array, target_array)

    # Test case 4: Test that the function raises a ValueError when the input arrays are not of the same length
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1, 0])
    with pytest.raises(ValueError):
        task_func(feature_array, target_array, feature_names=["f1", "f2", "f3", "f4", "f5"], target_name="target", seed=42)

    # Test case 5: Test that the function raises a ValueError when the input arrays are not of the same length
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1, 0])
    with pytest.raises(ValueError):
        task_func(feature_array, target_array, feature_names=["f1", "f2", "f3", "f4", "f5"], target_name="target", seed=42)