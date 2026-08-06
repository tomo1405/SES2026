import pytest
from src_0012 import task_func

def test_task_func():
    T1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    p25, p50, p75 = task_func(T1)
    assert isinstance(p25, float) and isinstance(p50, float) and isinstance(p75, float)
    assert 0 <= p25 <= 100 and 0 <= p50 <= 100 and 0 <= p75 <= 100
    T1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']]
    p25, p50, p75 = task_func(T1)
    assert isinstance(p25, float) and isinstance(p50, float) and isinstance(p75, float)
    assert 0 <= p25 <= 100 and 0 <= p50 <= 100 and 0 <= p75 <= 100