import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0431 import task_func


@pytest.fixture
def sample_data():
    df1 = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'feature1': [1.0, 2.0, 3.0, 4.0]
    })
    df2 = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'feature2': [4.0, 3.0, 2.0, 1.0]
    })
    return df1, df2

def test_task_func_output(sample_data):
    df1, df2 = sample_data
    labels, ax = task_func(df1, df2)
    
    assert isinstance(labels, np.ndarray)
    assert labels.shape == (4,)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_columns(sample_data):
    df1, df2 = sample_data
    labels, ax = task_func(df1, df2, column1="feature1", column2="feature2")
    
    assert isinstance(labels, np.ndarray)
    assert labels.shape == (4,)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_different_columns(sample_data):
    df1, df2 = sample_data
    # Add new columns to test with different feature names
    df1['featureA'] = df1['feature1']
    df2['featureB'] = df2['feature2']
    
    labels, ax = task_func(df1, df2, column1="featureA", column2="featureB")
    
    assert isinstance(labels, np.ndarray)
    assert labels.shape == (4,)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_no_common_id():
    df1 = pd.DataFrame({
        'id': [5, 6, 7, 8],
        'feature1': [1.0, 2.0, 3.0, 4.0]
    })
    df2 = pd.DataFrame({
        'id': [9, 10, 11, 12],
        'feature2': [4.0, 3.0, 2.0, 1.0]
    })
    
    with pytest.raises(KeyError):
        task_func(df1, df2)