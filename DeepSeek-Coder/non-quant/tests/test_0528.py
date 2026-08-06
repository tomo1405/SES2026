import pytest
from src_0528 import task_func
import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict

@pytest.fixture
def sample_data():
    return [
        {"key1": 1, "key2": 2},
        {"key1": 3, "key2": 4},
        {"key1": 5, "key2": 6}
    ]

def test_task_func(sample_data):
    results, ax = task_func("dummy_file.json")
    assert isinstance(results, dict)
    assert isinstance(ax, plt.Axes)
    assert len(results) == len(sample_data[0])