python
import pytest
from src_0947 import task_func

def test_task_func():
    # Test case 1: default values
    df = task_func()
    assert df.shape == (3, 2)
    assert df.values.min() >= 0 and df.values.max() <= 100
    
    # Test case 2: custom values
    df = task_func(rows=5, cols=3, min_val=10, max_val=20, seed=1)
    assert df.shape == (5, 3)
    assert df.values.min() >= 10 and df.values.max() <= 20
    
    # Test case 3: min_val == max_val
    df = task_func(rows=2, cols=3, min_val=100, max_val=100)
    assert df.shape == (2, 3)
    assert df.values.min() == 100 and df.values.max() == 100
    
    # Test case 4: invalid values
    with pytest.raises(ValueError):
        task_func(rows=2, cols=3, min_val=20, max_val=10)