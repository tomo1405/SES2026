import pytest
from src_0301 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Assuming src_0301 contains the function definition

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Value': [10, 20, 30]
    }
    df = pd.DataFrame(data)
    df = pd.DataFrame(data)

    # Call the function
    result_df, result_fig = task_func(df)

    # Add assertions to verify the output
    assert isinstance(result_df, pd.DataFrame), "The result should be a DataFrame"
    assert isinstance(result_fig, plt.Figure), "The result should be a matplotlib Figure"

    # Add more assertions as needed to verify the output

# Run the test
if __name__ == "__main__":
    pytest.main()