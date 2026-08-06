python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pytest

def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    if seed is not None:
        np.random.seed(seed)

    shuffled_array = feature_array.copy()
    np.random.shuffle(shuffled_array.T)

    df = pd.DataFrame(shuffled_array, columns=feature_names)
    df[target_name] = target_array

    clf = RandomForestClassifier()
    clf.fit(df[feature_names], df[target_name])

    return clf

def test_task_func():
    # Test case 1: Test with default parameters
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    target_array = np.array([0, 1, 0])
    clf = task_func(feature_array, target_array)
    assert clf.predict(feature_array) == target_array

    # Test case 2: Test with custom parameters
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    target_array = np.array([0, 1, 0])
    clf = task_func(feature_array, target_array, seed=42)
    assert clf.predict(feature_array) == target_array

    # Test case 3: Test with custom feature names
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    target_array = np.array([0, 1, 0])
    clf = task_func(feature_array, target_array, feature_names=["f1", "f2", "f3", "f4", "f5", "f6"])
    assert clf.predict(feature_array) == target_array

    # Test case 4: Test with custom target name
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    target_array = np.array([0, 1, 0])
    clf = task_func(feature_array, target_array, target_name="label")
    assert clf.predict(feature_array) == target_array

    # Test case 5: Test with invalid feature array shape
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16]])
    target_array = np.array([0, 1, 0])
    with pytest.raises(ValueError):
        clf = task_func(feature_array, target_array)

    # Test case 6: Test with invalid target array shape
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    target_array = np.array([0, 1, 0, 1])
    with pytest.raises(ValueError):
        clf = task_func(feature_array, target_array)