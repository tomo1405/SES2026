import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from src_0293 import task_func
import pytest

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'id': [1, 1, 2, 2, 3],
        'age': [20, 30, 25, 35, 40],
        'income': [50000, 60000, 70000, 80000, 90000]
    })

def test_task_func(sample_df):
    df_grouped, (hist, bins) = task_func(sample_df)
    assert isinstance(df_grouped, pd.DataFrame)
    assert isinstance(hist, np.ndarray)
    assert isinstance(bins, np.ndarray)
    assert len(hist) == 10
    assert len(bins) == 11
    assert (bins[1:] - bins[:-1]).all()
    assert (df_grouped['age'] >= 0).all() and (df_grouped['age'] <= 1).all()
    assert (df_grouped['income'] >= 0).all() and (df_grouped['income'] <= 1).all()