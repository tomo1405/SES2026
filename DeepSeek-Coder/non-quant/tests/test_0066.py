import pytest
from src_0066 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mock data for testing
data = [
    ['value1', 'value2', 'value3'],
    ['value4', 'value5', 'value6']
]

def test_task_func():
    result, _ = task_func(data)
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0

# Add more tests as needed to cover different scenarios