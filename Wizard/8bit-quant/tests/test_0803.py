python
import pytest
from src_0803 import task_func

def test_task_func():
    # Test valid inputs
    matrix, flat_list = task_func(2)
    assert matrix.shape == (2, 2)
    assert len(flat_list) == 4
    assert all(isinstance(x, int) for x in flat_list)
    assert all(1 <= x <= 100 for x in flat_list)
    
    matrix, flat_list = task_func(3)
    assert matrix.shape == (3, 3)
    assert len(flat_list) == 9
    assert all(isinstance(x, int) for x in flat_list)
    assert all(1 <= x <= 100 for x in flat_list)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        task_func(-1)
        
    with pytest.raises(ValueError):
        task_func(0)