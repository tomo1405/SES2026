import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0977 import task_func

def test_task_func_valid_input():
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df = task_func(records)
    assert isinstance(df, pd.DataFrame)

def test_task_func_ndim_check():
    records = np.array([1, 2, 3])
    with pytest.raises(ValueError) as excinfo:
        task_func(records)
    assert "Input must be a 2D numpy array." in str(excinfo.value)

def test_task_func_random_seed():
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df1 = task_func(records, random_seed=0)
    df2 = task_func(records, random_seed=0)
    assert df1.equals(df2)

def test_task_func_scaler():
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df = task_func(records)
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(records)
    assert np.array_equal(df.values, normalized_records)

def test_task_func_features():
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df = task_func(records)
    features = [f"f{i+1}" for i in range(records[0].shape[0])]
    np.random.shuffle(features)
    assert df.columns.tolist() == features