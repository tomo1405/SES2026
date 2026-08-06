import pytest
from src_0980 import task_func
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def test_task_func():
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    feature_names = ["f1", "f2", "f3", "f4", "f5"]
    target_name = "target"
    seed = 42

    clf = task_func(feature_array, target_array, feature_names, target_name, seed)

    assert isinstance(clf, RandomForestClassifier)
    assert clf.n_estimators == 100
    assert clf.random_state == seed
    assert clf.n_jobs == -1

    shuffled_array = feature_array.copy()
    np.random.shuffle(shuffled_array.T)

    df = pd.DataFrame(shuffled_array, columns=feature_names)
    df[target_name] = target_array

    assert np.array_equal(clf.feature_importances_, df[feature_names].T)
    assert np.array_equal(clf.predict(df[feature_names]), df[target_name])