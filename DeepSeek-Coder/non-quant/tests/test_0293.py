import pytest
from src_0293 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Assuming the function is defined in src_0293

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

    # Add assertions to verify the output
    assert isinstance(result, tuple)
    df_grouped, (hist, bins) = result
    assert isinstance(df_grouped, pd.DataFrame)
    assert isinstance(hist, np.ndarray)
    assert isinstance(bins, np.ndarray)
    assert len(hist) == 10