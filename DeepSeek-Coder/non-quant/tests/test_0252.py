import pytest
from src_0252 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Test cases for the function
def test_task_func():
    # Create a sample DataFrame
    data = pd.DataFrame({
        'Job': ['A', 'B', 'A', 'C', 'B', 'A']
    })

    # Call the function
    fig = task_func(data)

    # Assertions to check the output
    assert fig is not None
    assert isinstance(fig, plt.Figure)

# Run the tests
if __name__ == "__main__":
    pytest.main()