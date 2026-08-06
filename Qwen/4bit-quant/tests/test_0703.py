import pytest
from src_0703 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1]
    }
    return pd.DataFrame(data)

def test_task_func_output_shape(sample_data):
    result = task_func(sample_data)
    assert result.shape == (5, 2), "The output should have 2 columns (PC1 and PC2) for each of the 5 rows."

def test_task_func_column_names(sample_data):
    result = task_func(sample_data)
    assert list(result.columns) == ['PC1', 'PC2'], "The output DataFrame should have columns named 'PC1' and 'PC2'."

def test_task_func_values(sample_data):
    result = task_func(sample_data)
    expected_values = np.array([
        [-3.16227766, 0.],
        [-1.58113883, 0.],
        [0., 0.],
        [1.58113883, 0.],
        [3.16227766, 0.]
    ])
    np.testing.assert_allclose(result.values, expected_values, rtol=1e-5, atol=1e-8, err_msg="The values in the output DataFrame do not match the expected PCA transformation.")

def test_task_func_empty_input():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(empty_df)

def test_task_func_single_row_input(sample_data):
    single_row_df = sample_data.head(1)
    result = task_func(single_row_df)
    assert result.shape == (1, 2), "The output should have 2 columns (PC1 and PC2) for a single row."