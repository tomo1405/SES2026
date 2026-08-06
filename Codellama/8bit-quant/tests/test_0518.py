import pytest
from src_0518 import task_func
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def test_task_func():
    array = [1, 2, 3, 4, 5]
    random_seed = 42
    expected_df = pd.DataFrame(array)
    expected_transformed_data = np.array([[1, 2], [3, 4], [5, 6]])

    df, transformed_data = task_func(array, random_seed)

    assert df.equals(expected_df)
    assert np.allclose(transformed_data, expected_transformed_data)