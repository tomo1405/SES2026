import pytest
from src_1027 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

@pytest.fixture
def setup():
    return {
        "group1": [1, 2, 3, 4, 5],
        "group2": [2, 3, 4, 5, 6]
    }

def test_task_func(setup):
    result = task_func(setup)
    assert "significant" in result
    assert "group1_stats" in result
    assert "group2_stats" in result
    assert "ax_boxplot" in result
    assert "ax_histogram" in result
    assert "significant" in result

    # Add more assertions to check the correctness of the results