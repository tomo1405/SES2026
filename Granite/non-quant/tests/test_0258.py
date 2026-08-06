import pytest
from src_0258 import task_func
import numpy as np
import math

def test_task_func():
    ax = np.array([1, 2, 3])
    num_turns = 2
    expected_output = np.array([1, 2, 3])
    
    actual_output = task_func(ax, num_turns)
    
    assert np.array_equal(actual_output, expected_output)