import pytest
from src_0071 import task_func
import pandas as pd
import numpy as np
import json

# Mock data for testing
mock_data = {
    "email": ["example1@example.com", "example2@example.com"],
    "list": [1, 2]
}

def test_task_func():
    # Test with valid JSON data
    with open("mock_data.json", "w") as f:
        json.dump(mock_data, f)
    
    result = task_func("mock_data.json")
    assert isinstance(result, tuple)
    assert isinstance(result[0], pd.DataFrame)
    assert len(result[0].columns) == 4
    assert "sum" in result[0].columns
    assert "mean" in result[0].columns

    # Clean up
    import os
    os.remove("mock_data.json")