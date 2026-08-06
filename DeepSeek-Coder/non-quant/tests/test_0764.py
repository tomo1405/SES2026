import pytest
from src_0764 import task_func
import json
import csv
import numpy as np
from collections import defaultdict

# Test cases
def test_task_func():
    # Test case 1
    input_data = {
        "input_file": "test_input.json",
        "output_file": "test_output.csv"
    }
    expected_output = {
        "key1": {"mean": 1.5, "median": 1.5},
        "key2": {"mean": 3.5, "median": 3.5}
    }
    
    # Mock the input file content
    with open("test_input.json", "w") as f:
        json.dump([{"key1": 1, "key2": 2}, {"key1": 2, "key2": 4}], f)
    
    # Call the function
    result = task_func(input_data["input_file"], input_data["output_file"])
    
    # Read the output file and check the result
    with open(input_data["output_file"], "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert rows == [
            {"key": "key1", "mean": "1.5", "median": "1.5"},
            {"key": "key2", "mean": "3.5", "median": "3.5"}
        ]
    
    # Clean up
    import os
    os.remove("test_input.json")
    os.remove("test_output.csv")