import pytest
from src_0137 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Test cases for the function
def test_task_func():
    # Test with a valid DataFrame
    data = pd.DataFrame({
        'Feature1': [1, 2, 3, 4],
        'Feature2': [4, 3, 2, 1]
    })
    result, _ = task_func(data)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 4, "The result should have the same number of rows as the input DataFrame"

    # Test with an empty DataFrame
    empty_data = pd.DataFrame({
        'Feature1': [],
        'Feature2': []
    })
    with pytest.raises(ValueError, match="DataFrame is empty"):
        task_func(empty_data)

    # Test with a non-DataFrame input
    with pytest.raises(ValueError, match="Input must be a DataFrame"):
        task_func("not a DataFrame")

    # Test with a non-empty DataFrame
    data = pd.DataFrame({
        'Feature1': [1, 2, 3, 4],
        'Feature2': [4, 3, 2, 1]
    })
    result, _ = task_func(data)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 4, "The result should have the same number of rows as the input DataFrame"

    # Test the plotting part (this is more of a visual check, not a strict unit test)
    plt.show()  # This will open a window to display the plot