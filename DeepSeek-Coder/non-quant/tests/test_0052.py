import pytest
from src_0052 import task_func
import pandas as pd
import numpy as np

# Sample DataFrame for testing
data = {
    "Age": [25, 30, 35, 40, 45],
    "Height": [160, 165, 170, 175, 180]
}
df = pd.DataFrame(data)

def test_task_func():
    result, _ = task_func(df, 30, 170)
    assert len(result) > 0, "The result should not be empty"
    assert "Cluster" in result.columns, "The result should include a 'Cluster' column"

    # Add more assertions as needed to cover different scenarios