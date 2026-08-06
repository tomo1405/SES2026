import pytest
import numpy as np
import pandas as pd
from src_0164 import task_func

def test_task_func():
    # Test with valid input
    ax = task_func(rows=5, cols=5)
    assert ax is not None

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(rows=5, cols=6)