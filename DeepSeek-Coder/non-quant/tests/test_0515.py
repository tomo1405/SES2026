import pytest
from src_0515 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test data
    data = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 5, 7, 9]
    ]
    
    # Call the function
    result, _ = task_func(data)
    
    # Assertions
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 3, "The DataFrame should have 3 rows"
    assert len(result.columns) == 5, "The DataFrame should have 5 columns"

    # Additional assertions to check the plot
    # This is a bit tricky without actual plotting, so we'll check the basics
    assert plt.fignum_exists(1), "The plot should be created"

pytest.main()