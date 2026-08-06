import pytest
from src_0123 import task_func
import numpy as np
import random

def test_task_func():
    # Test with an empty list
    result = task_func([])
    assert isinstance(result, np.ndarray), "The result should be a numpy array"
    assert len(result) == sum([0]), "The length of the result should be the sum of the input list"

    # Add more test cases as needed