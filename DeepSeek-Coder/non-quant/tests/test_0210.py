import pytest
from src_0210 import task_func
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

@pytest.fixture
def sample_data():
    return [(1, 2), (2, 3), (3, 4), (4, 5)]

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert result is not None
    assert isinstance(result, plt.Axes)
    assert len(result.get_lines()) == 2
    assert len(result.get_children()) == 4