import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src_0980 import task_func
import pytest

@pytest.fixture
def feature_array():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

@pytest.fixture
def target_array():
    return np.array([0, 1, 0])

def test_task_func_with_seed(feature_array, target_array):
    seed = 42
    clf = task_func(feature_array, target_array, seed=seed)
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_without_seed(feature_array, target_array):
    clf = task_func(feature_array, target_array)
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_with_custom_feature_names(feature_array, target_array):
    feature_names = ["feature1", "feature2", "feature3"]
    clf = task_func(feature_array, target_array, feature_names=feature_names)
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_with_custom_target_name(feature_array, target_array):
    target_name = "label"
    clf = task_func(feature_array, target_array, target_name=target_name)
    assert isinstance(clf, RandomForestClassifier)