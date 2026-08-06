import pytest
from src_0231 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame for testing
sample_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Country': ['USA', 'Canada', 'USA', 'Canada'],
    'Score': [85, 90, 88, 92]
})

def test_task_func():
    # Test with valid DataFrame
    result = task_func(sample_data)
    assert isinstance(result, plt.Figure)

    # Add more tests as needed