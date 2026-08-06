python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    if random_seed is not None:
        np.random.seed(random_seed)

    if not (records.ndim == 2):
        raise ValueError("Input must be a 2D numpy array.")

    records_copy = records.copy()
    np.random.shuffle(records_copy.T)

    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(records_copy)

    features = [f"f{i+1}" for i in range(records[0].shape[0])]
    np.random.shuffle(features)

    df = pd.DataFrame(normalized_records, columns=features)

    return df

def test_task_func():
    # Test case 1: Test with valid input
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    random_seed = 0
    expected_df = pd.DataFrame([[0.0, -1.0, 1.0], [-1.0, 0.0, -1.0], [1.0, 1.0, 0.0]], columns=['f1', 'f2', 'f3'])
    assert task_func(records, random_seed).equals(expected_df)

    # Test case 2: Test with invalid input (not 2D numpy array)
    records = np.array([1, 2, 3])
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(records, random_seed)

    # Test case 3: Test with random seed
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    random_seed = 1
    expected_df = pd.DataFrame([[0.0, -1.0, 1.0], [-1.0, 0.0, -1.0], [1.0, 1.0, 0.0]], columns=['f1', 'f2', 'f3'])
    assert task_func(records, random_seed).equals(expected_df)