import pytest
from src_0235 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [70, 80, 85, 90]
    }
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(df)

    # Assertions
    assert isinstance(result, tuple), "The function should return a tuple."
    assert len(result) == 2, "The function should return a tuple with two elements."
    assert isinstance(result[0], plt.Figure), "The first element should be a matplotlib figure."
    assert isinstance(result[1], plt.Axes), "The second element should be a matplotlib Axes object."

    # Clean up
    plt.close('all')