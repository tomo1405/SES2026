import pytest
from src_0400 import task_func
import numpy as np
import matplotlib.pyplot as plt
import math

def test_task_func():
    # Test with valid input
    frequency = 2
    sample_size = 10000
    fig, ax = task_func(frequency, sample_size=sample_size)
    assert fig is not None
    assert ax is not None
    assert len(ax.lines) == 2  # sin and cos lines
    assert ax.get_title() == ''  # No title
    assert ax.get_xlabel() == 'x'  # Default xlabel
    assert ax.get_ylabel() == 'y'  # Default ylabel

    # Test with invalid frequency
    with pytest.raises(ValueError):
        task_func(-1)

    # Test with invalid sample size
    with pytest.raises(ValueError):
        task_func(2, sample_size=0)