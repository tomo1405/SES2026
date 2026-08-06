import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src_0980 import task_func

def test_task_func():
    feature_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    target_array = np.array([0, 1, 0])
    feature_names = ["f1", "f2", "f3"]
    target_name = "target"
    seed = 42

    clf = task_func(feature_array, target_array, feature_names, target_name, seed)

    assert isinstance(clf, RandomForestClassifier)
    assert clf.feature_names_in_ == feature_names
    assert clf.target_name_ == target_name