import pytest
from src_0299 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame for testing
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Value': [10, 20, 30]
}
df = pd.DataFrame(data)

def test_task_func():
    result, _ = task_func(df)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"

def test_plot():
    _, ax = task_func(df, plot=True)
    assert ax is not None, "The plot should be created"

# Add more tests as needed