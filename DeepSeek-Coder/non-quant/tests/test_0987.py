import pytest
from src_0987 import task_func
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Test cases
def test_task_func():
    # Test case 1: Basic functionality
    json_data = '{"key1": {"key2": [1, 2, 3, 4, 5]}'
    key_path = ["key1", "key2"]
    result = task_func(json_data, key_path)
    assert result is not None

    # Add more test cases as needed

# Add more test cases as needed