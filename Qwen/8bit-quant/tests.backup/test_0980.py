import pytest
from src_0980 import task_func
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def test_task_func_output_type():
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    clf = task_func(feature_array, target_array)
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_dataframe_columns():
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    clf = task_func(feature_array, target_array)
    df = pd.DataFrame(feature_array, columns=["f1", "f2", "f3", "f4", "f5"])
    df["target"] = target_array
    assert list(clf.feature_names_in_) == list(df.columns[:-1])

def test_task_func_shuffle():
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    clf1 = task_func(feature_array, target_array, seed=42)
    clf2 = task_func(feature_array, target_array, seed=42)
    assert not np.array_equal(clf1.feature_importances_, clf2.feature_importances_)

def test_task_func_with_custom_feature_names():
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    custom_feature_names = ["a", "b", "c", "d", "e"]
    clf = task_func(feature_array, target_array, feature_names=custom_feature_names)
    df = pd.DataFrame(feature_array, columns=custom_feature_names)
    df["target"] = target_array
    assert list(clf.feature_names_in_) == list(df.columns[:-1])

def test_task_func_with_custom_target_name():
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    custom_target_name = "label"
    clf = task_func(feature_array, target_array, target_name=custom_target_name)
    df = pd.DataFrame(feature_array, columns=["f1", "f2", "f3", "f4", "f5"])
    df[custom_target_name] = target_array
    assert list(clf.feature_names_in_) == list(df.columns[:-1])