import pytest
from src_0641 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def mock_random(monkeypatch):
    def mock_randint(low, high, size=None):
        return np.full(size, 500)  # Return a constant value for testing
    monkeypatch.setattr(np.random, 'randint', mock_randint)

def test_task_func(mock_random):
    df = task_func()
    
    # Check DataFrame structure
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (12, 5)
    assert all(df.index == ['Month' + str(i) for i in range(1, 13)])
    assert all(df.columns == ['Product' + str(i) for i in range(1, 6)])
    
    # Check that all values are 500 due to mocking
    assert (df.values == 500).all()

def test_task_func_data_range(mock_random):
    df = task_func()
    
    # Check that all values are within the specified range
    assert (df.values >= 100).all() and (df.values <= 1000).all()

def test_task_func_visualizations(monkeypatch):
    # Mocking plt.show to prevent actual plotting
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    # Run the function to trigger visualizations
    task_func()