import pytest
from src_0528 import task_func
import json
import numpy as np
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

# Mock data for testing
mock_data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "b": 5, "c": 6},
    {"a": 7, "b": 8, "c": 9}
]

# Create a temporary JSON file for testing
@pytest.fixture
def temp_json_file(tmp_path):
    json_file = tmp_path / "temp.json"
    with open(json_file, "w") as f:
        json.dump(mock_data, f)
    return json_file

def test_task_func(temp_json_file):
    results, ax = task_func(str(temp_json_file))
    
    # Check if the results dictionary is correctly computed
    expected_results = {
        "a": {"mean": np.mean([1, 4, 7]), "median": np.median([1, 4, 7])},
        "b": {"mean": np.mean([2, 5, 8]), "median": np.median([2, 5, 8])},
        "c": {"mean": np.mean([3, 6, 9]), "median": np.median([3, 6, 9])}
    }
    assert results == expected_results
    
    # Check if the Axes object is correctly created
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Boxplot of Values for Each Key"
    
    # Clean up the plot
    plt.close(ax.figure)