import pytest
from src_0670 import task_func

def test_task_func():
    input_data = {'a': 0, 'b': math.pi/2, 'c': math.pi, 'd': 3*math.pi/2}
    expected_output = ('a', 'd')
    
    result = task_func(input_data)
    
    assert result == expected_output