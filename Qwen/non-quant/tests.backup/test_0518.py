import pytest
from src_0518 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def test_task_func_output_types():
    array = [[1, 2], [3, 4], [5, 6]]
    df, transformed_data = task_func(array)
    
    assert isinstance(df, pd.DataFrame), "The first output should be a pandas DataFrame"
    assert isinstance(transformed_data, np.ndarray), "The second output should be a numpy ndarray"

def test_task_func_dataframe_content():
    array = [[1, 2], [3, 4], [5, 6]]
    df, _ = task_func(array)
    
    expected_df = pd.DataFrame(array)
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_pca_transformation():
    array = [[1, 2], [3, 4], [5, 6]]
    _, transformed_data = task_func(array)
    
    assert transformed_data.shape == (3, 2), "The transformed data should have 3 rows and 2 columns"

def test_task_func_random_state_consistency():
    array = [[1, 2], [3, 4], [5, 6]]
    _, transformed_data_1 = task_func(array, random_seed=42)
    _, transformed_data_2 = task_func(array, random_seed=42)
    
    assert np.array_equal(transformed_data_1, transformed_data_2), "The transformation results should be consistent with the same random seed"

def test_task_func_random_state_inconsistency():
    array = [[1, 2], [3, 4], [5, 6]]
    _, transformed_data_1 = task_func(array, random_seed=42)
    _, transformed_data_2 = task_func(array, random_seed=43)
    
    assert not np.array_equal(transformed_data_1, transformed_data_2), "The transformation results should differ with different random seeds"