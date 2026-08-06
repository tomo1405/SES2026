import pytest
from src_0295 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'id': [1, 1, 2, 2],
        'age': [25, 30, 35, 40],
        'income': [50000, 60000, 70000, 80000]
    }
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(df)

    # Add assertions to validate the output
    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2  # Assuming the grouping results in 2 groups