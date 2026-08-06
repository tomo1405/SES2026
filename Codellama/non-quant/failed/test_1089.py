import pytest
from src_1089 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    data = np.random.rand(100, 5)
    df = pd.DataFrame(data)
    df[df < 0.5] = 0

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    standardized_df = pd.DataFrame(scaled_data, columns=df.columns)

    assert np.allclose(task_func(data), standardized_df)

def test_task_func_with_none():
    assert np.allclose(task_func(), task_func(np.random.rand(100, 5)))