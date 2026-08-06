import pytest
from src_0950 import task_func

def test_task_func():
    # Test case 1: Default arguments
    df = task_func(rows=5, columns=3)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 3)
    
    # Test case 2: Custom seed
    df = task_func(rows=5, columns=3, seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 3)
    assert df.iloc[0, 0] == 0.134364
    
    # Test case 3: Invalid arguments
    with pytest.raises(ValueError):
        df = task_func(rows=-1, columns=3)
    with pytest.raises(ValueError):
        df = task_func(rows=5, columns=-3)