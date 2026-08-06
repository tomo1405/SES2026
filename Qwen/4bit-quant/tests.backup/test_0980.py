import pytest
from src_0980 import task_func
import numpy as np
import pandas as pd

def test_task_func_with_default_seed():
    # Test with default seed
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    
    clf = task_func(feature_array, target_array, seed=42)
    
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_without_seed():
    # Test without setting a seed
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    
    clf = task_func(feature_array, target_array)
    
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_with_custom_feature_names():
    # Test with custom feature names
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    feature_names = ["feature1", "feature2", "feature3", "feature4", "feature5"]
    
    clf = task_func(feature_array, target_array, feature_names=feature_names, seed=42)
    
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_with_custom_target_name():
    # Test with custom target name
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    target_array = np.array([0, 1])
    target_name = "label"
    
    clf = task_func(feature_array, target_array, target_name=target_name, seed=42)
    
    assert isinstance(clf, RandomForestClassifier)

def test_task_func_with_different_array_sizes():
    # Test with different sizes of feature and target arrays
    feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
    target_array = np.array([0, 1])
    
    with pytest.raises(ValueError) as excinfo:
        task_func(feature_array, target_array, seed=42)
    
    assert "Data cardinality mismatch" in str(excinfo.value)

def test_task_func_with_empty_arrays():
    # Test with empty arrays
    feature_array = np.array([])
    target_array = np.array([])
    
    with pytest.raises(ValueError) as excinfo:
        task_func(feature_array, target_array, seed=42)
    
    assert "Data cardinality mismatch" in str(excinfo.value)