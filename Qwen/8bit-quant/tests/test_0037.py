import pytest
from src_0037 import task_func
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Mocking plt.show to prevent actual plotting during tests
plt.show = lambda: None

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'A': [2, 3, 5],
        'B': [1, 3, 4],
        'C': [0, 0, 0]
    })

def test_task_func_positive_values_only(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df)

def test_task_func_valid_input(sample_df):
    # Replace non-target values with positive values
    sample_df['A'] = sample_df['A'].apply(lambda x: 3 if x != 3 else x)
    transformed_df, fig = task_func(sample_df)
    
    # Check if transformed_df contains only target values or zeros
    assert all(transformed_df.values.flatten() in TARGET_VALUES)

def test_task_func_constant_data(sample_df):
    # Make one of the columns constant
    sample_df['A'] = 3
    transformed_df, fig = task_func(sample_df)
    
    # Check if the constant column remains unchanged
    assert all(transformed_df['A'] == 3)

def test_task_func_non_constant_data(sample_df):
    # Replace non-target values with positive values
    sample_df['A'] = sample_df['A'].apply(lambda x: 3 if x != 3 else x)
    transformed_df, fig = task_func(sample_df)
    
    # Check if the non-constant column is transformed
    assert not all(transformed_df['A'] == 3)

def test_task_func_plotting(sample_df):
    # Replace non-target values with positive values
    sample_df['A'] = sample_df['A'].apply(lambda x: 3 if x != 3 else x)
    transformed_df, fig = task_func(sample_df)
    
    # Check if the figure object is created
    assert isinstance(fig, plt.Figure)