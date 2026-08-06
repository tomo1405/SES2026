import pytest
from src_0641 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def mock_random(monkeypatch):
    def mock_randint(low, high, size=None):
        return np.full(size, 500)  # Fixed value for reproducibility
    monkeypatch.setattr(np.random, 'randint', mock_randint)

def test_task_func(mock_random):
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (12, 5)
    assert list(df.index) == ['Month' + str(i) for i in range(1, 13)]
    assert list(df.columns) == ['Product' + str(i) for i in range(1, 6)]
    assert all(df.values.flatten() == 500)  # Due to mock_random fixture