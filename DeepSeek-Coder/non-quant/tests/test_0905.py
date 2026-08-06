import pytest
from src_0905 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Define a sample DataFrame for testing
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [5, 4, 3, 2, 1],
    'z': [1, 3, 2, 5, 4]
}

def test_task_func():
    # Test the function with the sample data
    result = task_func(data)
    
    # Assertions to check the output
    assert result is not None
    assert isinstance(result, plt.Axes)

# Run the test
if __name__ == "__main__":
    pytest.main()