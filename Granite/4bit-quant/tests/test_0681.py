import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src_0681 import task_func
import pytest

def test_task_func():
    # Create a sample DataFrame with numerical and categorical features
    df = pd.DataFrame({
        'num_feature1': np.random.rand(100),
        'num_feature2': np.random.rand(100),
        'cat_feature1': np.random.choice(['A', 'B', 'C'], 100),
        'cat_feature2': np.random.choice(['X', 'Y', 'Z'], 100)
    })

    # Test the function with no features specified
    features = []
    expected_df = df.copy()
    actual_df = task_func(df, features)
    assert actual_df.equals(expected_df)

    # Test the function with some numerical features specified
    features = ['num_feature1', 'num_feature2']
    expected_df = df.copy()
    expected_df.loc[:, features] = StandardScaler().fit_transform(expected_df.loc[:, features])
    actual_df = task_func(df, features)
    assert actual_df.equals(expected_df)

    # Test the function with some categorical features specified
    features = ['cat_feature1', 'cat_feature2']
    with pytest.raises(ValueError):
        task_func(df, features)