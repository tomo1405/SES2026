import pytest
from src_0450 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [2, 3, 4, 5, 6],
        "Feature4": [6, 7, 8, 9, 10],
        "Feature5": [1, 3, 5, 7, 9]
    })

    # Call the function
    result, _ = task_func(data)

    # Check the output
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (5, 5), "The shape of the result should be (5, 5)"

    # Check the plots
    _, axes = plt.subplots()
    task_func(data)
    assert len(axes) == len(data.columns), "The number of axes should match the number of features"

    # Clean up
    plt.close()