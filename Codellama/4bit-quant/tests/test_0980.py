import numpy as np
from src_0980 import task_func


def test_task_func():
    # Test with random data
    feature_array = np.random.rand(100, 5)
    target_array = np.random.randint(0, 2, size=100)
    clf = task_func(feature_array, target_array)
    assert isinstance(clf, RandomForestClassifier)

    # Test with known data
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    clf = task_func(feature_array, target_array)
    assert isinstance(clf, RandomForestClassifier)

    # Test with different feature names
    feature_array = np.random.rand(100, 5)
    target_array = np.random.randint(0, 2, size=100)
    clf = task_func(feature_array, target_array, feature_names=["f1", "f2", "f3", "f4", "f5"])
    assert isinstance(clf, RandomForestClassifier)

    # Test with different target name
    feature_array = np.random.rand(100, 5)
    target_array = np.random.randint(0, 2, size=100)
    clf = task_func(feature_array, target_array, target_name="target")
    assert isinstance(clf, RandomForestClassifier)

    # Test with different seed
    feature_array = np.random.rand(100, 5)
    target_array = np.random.randint(0, 2, size=100)
    clf = task_func(feature_array, target_array, seed=42)
    assert isinstance(clf, RandomForestClassifier)