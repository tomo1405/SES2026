import pytest
import numpy as np
import pandas as pd
from src_0950 import task_func

def test_task_func():
    # Test case 1: Default parameters
    df = task_func(rows=3, columns=4)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)
    
    # Test case 2: Custom seed and shape
    df = task_func(rows=5, columns=6, seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 6)
    assert df.iloc[0, 0] == 0.399207843137
    
    # Test case 3: Invalid input
    with pytest.raises(ValueError):
        task_func(rows=-1, columns=2)
    with pytest.raises(ValueError):
        task_func(rows=2, columns=-1)