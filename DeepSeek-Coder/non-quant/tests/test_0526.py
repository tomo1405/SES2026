import pytest
from src_0526 import task_func
import json
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

@pytest.fixture
def sample_data():
    return [
        {"key1": [1, 2, 3, 4, 5], "key2": [10, 20, 30, 40, 50]},
        {"key1": [1, 2, 3, 4, 5], "key2": [10, 20, 30, 40, 50]}
    ]

def test_task_func(sample_data):
    result, plots = task_func("dummy_file.json")
    assert isinstance(result, dict), "Result should be a dictionary"
    assert all(isinstance(v, dict) for v in result.values()), "Each result value should be a dictionary"
    assert all(isinstance(k, str) for k in result.keys()), "Keys should be strings"
    assert all(isinstance(v["mean"], (int, float)) for v in result.values()), "Mean values should be numbers"
    assert all(isinstance(v["mean"], (int, float)) for v in result.values()), "Mean values should be numbers"
    assert all(isinstance(v["median"], (int, float)) for v in result.values()), "Median values should be numbers"
    assert len(plots) == len(result), "Number of plots should match the number of result items"
    plt.close()  # Close the plots to avoid memory leaks