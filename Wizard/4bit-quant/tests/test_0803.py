python
import pytest
from src_0803 import task_func

def test_task_func():
    # Test case 1: dimension <= 0
    with pytest.raises(ValueError):
        task_func(0)
    
    # Test case 2: dimension > 0
    matrix, flat_list = task_func(5)
    assert isinstance(matrix, np.ndarray)
    assert isinstance(flat_list, list)
    assert len(flat_list) == 25
    assert len(set(flat_list)) == 25
    assert len(set(matrix.flatten().tolist())) == 25