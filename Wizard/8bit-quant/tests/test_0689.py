python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0689 import task_func

def test_task_func():
    # Create sample data
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Test standardization
    df_standardized = task_func(df)
    assert df_standardized.shape == (3, 2)
    assert df_standardized.mean().sum() == 0
    assert df_standardized.std().sum() == 1