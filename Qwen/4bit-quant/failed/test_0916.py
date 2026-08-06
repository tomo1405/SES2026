import pytest
from src_0916 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'closing_price': [100, 102, 101, 105, 110, 1000, 103]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    outliers, ax = task_func(sample_df)
    
    # Check if the outliers DataFrame is correctly identified
    expected_outliers = sample_df.iloc[[5]]
    assert outliers.equals(expected_outliers), "The identified outliers do not match the expected result."
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes), "The function did not return a matplotlib Axes object."

def test_task_func_with_custom_threshold(sample_df):
    outliers, ax = task_func(sample_df, z_threshold=3)
    
    # Check if no outliers are found with a higher threshold
    assert outliers.empty, "Outliers were found with a higher Z-Score threshold."

def test_task_func_with_no_outliers(sample_df):
    # Modify the dataframe to have no outliers
    sample_df['closing_price'] = [100, 102, 101, 105, 110, 103]
    outliers, ax = task_func(sample_df)
    
    # Check if no outliers are found
    assert outliers.empty, "Outliers were found when there should be none."

def test_task_func_with_all_outliers(sample_df):
    # Modify the dataframe to have all entries as outliers
    sample_df['closing_price'] = [1000, 1000, 1000, 1000, 1000, 1000, 1000]
    outliers, ax = task_func(sample_df)
    
    # Check if all entries are identified as outliers
    assert outliers.equals(sample_df), "Not all entries were identified as outliers."