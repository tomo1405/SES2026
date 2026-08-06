import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src_0681 import task_func
import pytest

# Create a sample DataFrame for testing
df = pd.DataFrame({
    'feature1': np.random.normal(0, 1, 100),
    'feature2': np.random.normal(5, 2, 100),
    'feature3': np.random.normal(10, 3, 100)
})

# Test case 1: No features are specified
features = []
expected_df = df.copy()
expected_df['dummy'] = np.zeros(len(df))

result_df = task_func(df, features)

assert result_df.equals(expected_df)

# Test case 2: Some features are specified
features = ['feature1', 'feature2']
expected_df = df.copy()
expected_df.loc[:, features] = pd.DataFrame(StandardScaler().fit_transform(df.loc[:, features]), columns=features, index=df.index)
expected_df['dummy'] = np.zeros(len(df))

result_df = task_func(df, features)

assert result_df.equals(expected_df)

# Test case 3: All features are specified
features = ['feature1', 'feature2', 'feature3']
expected_df = df.copy()
expected_df.loc[:, features] = pd.DataFrame(StandardScaler().fit_transform(df.loc[:, features]), columns=features, index=df.index)
expected_df['dummy'] = np.zeros(len(df))

result_df = task_func(df, features)

assert result_df.equals(expected_df)