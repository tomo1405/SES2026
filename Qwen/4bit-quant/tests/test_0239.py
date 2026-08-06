import pytest
from src_0239 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Score': [80, 85, 90, 80]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    df, ax = task_func(sample_df)
    
    # Check for duplicates removal
    assert df.shape[0] == 3, "Duplicate names were not removed correctly"
    
    # Check for standardized values
    assert np.allclose(df['Age'].mean(), 0, atol=1e-6), "Age values are not standardized"
    assert np.allclose(df['Score'].mean(), 0, atol=1e-6), "Score values are not standardized"
    
    # Check for plot properties
    assert ax.get_xlabel() == 'Age (standardized)', "X-axis label is incorrect"
    assert ax.get_ylabel() == 'Score (standardized)', "Y-axis label is incorrect"
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score', "Plot title is incorrect"
    assert len(ax.collections) > 0, "No scatter plot was created"