import pytest
from src_0794 import task_func

def test_task_func():
    assert task_func().tolist() == ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'A', 'B', 'C']
    assert task_func(l=['A', 'B', 'C']).tolist() == ['C', 'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    with pytest.raises(ValueError):
        task_func(l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])