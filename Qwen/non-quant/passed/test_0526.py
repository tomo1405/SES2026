import pytest
from src_0526 import task_func
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from io import StringIO

def test_task_func_with_valid_json(tmp_path):
    # Create a temporary JSON file with sample data
    data = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4}
    ]
    json_file = tmp_path / "data.json"
    with open(json_file, "w") as f:
        json.dump(data, f)

    # Call the function
    result, plots = task_func(str(json_file))

    # Check the result dictionary
    expected_result = {
        "a": {"mean": 2.0, "median": 2.0},
        "b": {"mean": 3.0, "median": 3.0}
    }
    assert result == expected_result

    # Check the number of plots
    assert len(plots) == 2

def test_task_func_with_empty_json(tmp_path):
    # Create a temporary JSON file with empty data
    data = []
    json_file = tmp_path / "empty_data.json"
    with open(json_file, "w") as f:
        json.dump(data, f)

    # Call the function
    result, plots = task_func(str(json_file))

    # Check the result dictionary
    expected_result = {}
    assert result == expected_result

    # Check the number of plots
    assert len(plots) == 0

def test_task_func_with_single_entry_json(tmp_path):
    # Create a temporary JSON file with a single entry
    data = [{"a": 5}]
    json_file = tmp_path / "single_entry.json"
    with open(json_file, "w") as f:
        json.dump(data, f)

    # Call the function
    result, plots = task_func(str(json_file))

    # Check the result dictionary
    expected_result = {"a": {"mean": 5.0, "median": 5.0}}
    assert result == expected_result

    # Check the number of plots
    assert len(plots) == 1

def test_task_func_with_nonexistent_file():
    # Attempt to call the function with a non-existent file
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.json")