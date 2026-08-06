import pytest
from src_0920 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Define a sample data for testing
sample_data = {
    'column1': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'E', 'E', 'C', 'D']
}

def test_task_func():
    result = task_func(sample_data, 'column1')
    assert isinstance(result, plt.Axes)
    plt.close()