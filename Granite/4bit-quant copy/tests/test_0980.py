import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src_0980 import task_func

def test_task_func():
    feature_array = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
    target_array = np.array([0, 1])
    feature_names = ["f1", "f2", "f3", "f4", "f5"]
    target_name = "target"
    seed = 42

    clf = task_func(
        feature_array,
        target_array,
        feature_names=feature_names,
        target_name=target_name,
        seed=seed,
    )

    assert isinstance(clf, RandomForestClassifier)
    assert clf.classes_.shape == (2,)
    assert clf.classes_[0] == 0
    assert clf.classes_[1] == 1
    assert clf.n_classes_ == 2
    assert clf.n_features_ == 5
    assert clf.n_outputs_ == 1
    assert clf.random_state == 42