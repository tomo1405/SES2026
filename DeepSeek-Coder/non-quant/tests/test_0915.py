import pytest
from src_0915 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Assuming src_0915 contains the target function

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'closing_price': [100, 102, 104]
    }
    df = pd.DataFrame(data)
    df = pd.DataFrame(data)
    
    # Call the function
    result = task_func(df)
    
    # Assertions can be added here to verify the output
    assert isinstance(result, tuple)
    assert len(result) == 2
    pred_prices, ax = result
    assert isinstance(pred_prices, list)
    assert isinstance(ax, plt.Axes)

# Run the test
if __name__ == "__main__":
    pytest.main()