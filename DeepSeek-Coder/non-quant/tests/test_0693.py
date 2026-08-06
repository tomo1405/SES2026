import pytest
from src_0693 import task_func

def test_task_func():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    result = task_func(tuples_list)
    assert result.iloc[0, 0] == math.sin(1)
    assert result.iloc[1, 0] == math.sin(3)
    assert result.iloc[2, 0] == math.sin(5)
    assert result.iloc[0, 1] == math.sin(2)
    assert result.iloc[1, 1] == math.sin(4)
    assert result.iloc[2, 1] == math.sin(6)

    # Add more assertions as needed to cover different cases