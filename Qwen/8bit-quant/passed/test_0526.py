import pytest
from src_0526 import task_func
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import tempfile

@pytest.fixture
def sample_data():
    data = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
        {"a": 5, "b": 6}
    ]
    return data

@pytest.fixture
def temp_json_file(sample_data):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        json.dump(sample_data, tmp)
    yield tmp.name
    # Clean up the temporary file
    import os
    os.remove(tmp.name)

def test_task_func(temp_json_file, sample_data):
    expected_stats = {
        "a": {"mean": 3.0, "median": 3.0},
        "b": {"mean": 4.0, "median": 4.0}
    }
    result, plots = task_func(temp_json_file)
    
    assert result == expected_stats
    assert len(plots) == 2

    # Check if the plots are created correctly
    for i, key in enumerate(expected_stats.keys()):
        ax = plots[i]
        bars = ax.patches
        assert len(bars) == 2
        assert bars[0].get_height() == expected_stats[key]["mean"]
        assert bars[1].get_height() == expected_stats[key]["median"]
        assert ax.get_title() == f"Statistics of {key}"