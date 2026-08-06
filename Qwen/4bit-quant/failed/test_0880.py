import pytest
from src_0880 import task_func
import pandas as pd
import numpy as np

# Helper function to create a sample DataFrame
def create_sample_df():
    data = {
        'Category1': ['A', 'B', 'A', 'C', 'B', 'A'],
        'Category2': ['X', 'Y', 'X', 'Z', 'Y', 'X']
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_data():
    df = create_sample_df()
    p_value = task_func(df, 'Category1', 'Category2')
    assert isinstance(p_value, float)

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="The input DataFrame is empty."):
        task_func(df, 'Category1', 'Category2')

def test_task_func_with_missing_column():
    df = create_sample_df()
    with pytest.raises(ValueError, match="One or both of the columns 'Category3' and 'Category2' do not exist in the DataFrame."):
        task_func(df, 'Category3', 'Category2')

def test_task_func_with_numerical_data():
    df = create_sample_df()
    df['Category1'] = [1, 2, 1, 3, 2, 1]
    with pytest.raises(TypeError, match="One or both of the columns contain non-categorical data. The chi-square test requires categorical data."):
        task_func(df, 'Category1', 'Category2')

def test_task_func_with_single_category():
    df = create_sample_df()
    df['Category1'] = ['A', 'A', 'A', 'A', 'A', 'A']
    with pytest.raises(ValueError, match="One or both of the columns do not have multiple categories. The chi-square test requires variability in data."):
        task_func(df, 'Category1', 'Category2')

def test_task_func_with_small_counts():
    df = create_sample_df()
    df['Category2'] = ['X', 'X', 'X', 'X', 'X', 'X']
    with pytest.raises(ValueError, match="Some categories have less than 5 observations. This violates the assumptions of the chi-square test."):
        task_func(df, 'Category1', 'Category2')