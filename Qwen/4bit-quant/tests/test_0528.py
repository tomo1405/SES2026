import pytest
from src_0528 import task_func
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Mocking the input file content
MOCK_DATA = [
    {"a": 1, "b": 2},
    {"a": 3, "b": 4},
    {"a": 5, "b": 6}
]

@pytest.fixture
def mock_input_file(tmp_path):
    file_path = tmp_path / "mock_data.json"
    with open(file_path, "w") as f:
        json.dump(MOCK_DATA, f)
    return str(file_path)

def test_task_func(mock_input_file):
    results, ax = task_func(mock_input_file)
    
    # Check if the results dictionary is correct
    expected_results = {
        "a": {"mean": np.mean([1, 3, 5]), "median": np.median([1, 3, 5])},
        "b": {"mean": np.mean([2, 4, 6]), "median": np.median([2, 4, 6])}
    }
    assert results == expected_results
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Boxplot of Values for Each Key"
    
    # Check if the plot contains the correct data
    data = pd.DataFrame(MOCK_DATA).melt(var_name="X", value_name="Y")
    assert ax.collections[0].get_offsets().data.shape[0] == len(data)