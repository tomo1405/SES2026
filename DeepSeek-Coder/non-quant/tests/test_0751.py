import pytest
from src_0751 import task_func
import pandas as pd
import statsmodels.api as sm

# Define test cases
def test_task_func():
    # Create a sample DataFrame
    data = {
        'column1': [1, 2, 3, 4, 5],
        'column2': [5, 4, 3, 2, 1],
        'column3': [1, 2, 3, 4, 5],
        'column4': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)

    # Define parameters
    height = 2
    weight = 3
    columns = ['column1', 'column2', 'column3', 'column4']

    # Call the function
    result = task_func(df=df, height=height, weight=weight, columns=columns)

    # Add assertions to validate the output
    assert result is not None  # Assuming the function should return a valid result

# Run the test
if __name__ == "__main__":
    pytest.main()