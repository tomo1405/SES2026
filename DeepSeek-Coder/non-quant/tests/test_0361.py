import pytest
from src_0361 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Mocking the necessary imports and functions
class MockDataFrame:
    def __init__(self):
        self.columns = ['A', 'B', 'C']
        self.data = {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        }

    def __getitem__(self, key):
        return self.data[key]

    def mean(self):
        return np.mean(list(self.data.values()), axis=0)

    def std(self):
        return np.std(list(self.data.values()), axis=0)

@pytest.fixture
def mock_dataframe():
    return MockDataFrame()

def test_task_func(mock_dataframe):
    file_location = 'mock_file.xlsx'
    sheet_name = 'Sheet1'
    result, fig = task_func(file_location=file_location, sheet_name=sheet_name)

    assert isinstance(result, dict), "Result should be a dictionary"
    assert len(result) > 0, "Result should not be empty"
    assert isinstance(fig, plt.Figure), "Figure should be a matplotlib figure"

    # Add more assertions as needed to cover different scenarios