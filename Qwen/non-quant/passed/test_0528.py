import pytest
from src_0528 import task_func
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

@pytest.fixture
def sample_data_file(tmp_path):
    data = [
        {"key1": 1, "key2": 2},
        {"key1": 3, "key2": 4},
        {"key1": 5, "key2": 6}
    ]
    file_path = tmp_path / "sample_data.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return file_path

def test_task_func(sample_data_file):
    results, ax = task_func(str(sample_data_file))
    
    # Check if the results dictionary is correct
    expected_results = {
        "key1": {"mean": 3.0, "median": 3.0},
        "key2": {"mean": 4.0, "median": 4.0}
    }
    assert results == expected_results
    
    # Check if the Axes object is a matplotlib Axes instance
    assert isinstance(ax, plt.Axes)
    
    # Check if the plot title is set correctly
    assert ax.get_title() == "Boxplot of Values for Each Key"

    # Check if the plot contains the correct number of boxes
    lines = ax.get_lines()
    assert len(lines) == 2 * 6  # 2 keys, 6 whiskers and caps per box

    # Check if the plot contains the correct number of boxes
    boxes = ax.artists
    assert len(boxes) == 2  # 2 keys

    # Clean up the plot to avoid warnings
    plt.close(ax.figure)