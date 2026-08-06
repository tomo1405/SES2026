import pytest
import pandas as pd
from src_0433 import task_func

# Mock data for testing
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature1': ['A', 'B', 'A', 'C']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature2': ['X', 'Y', 'X', 'Z']
})

def test_task_func():
    # Expected output
    expected_p_value = 0.0  # This is a placeholder, actual value will depend on the data

    # Call the function
    p_value, heatmap = task_func(df1, df2)

    # Check if the returned p-value is of the correct type
    assert isinstance(p_value, float), "The p-value should be a float."

    # Check if the heatmap is of the correct type
    assert isinstance(heatmap, sns.axisgrid.FacetGrid), "The heatmap should be a seaborn heatmap object."

    # Check if the p-value is as expected (this is a placeholder check)
    assert p_value == expected_p_value, f"The p-value should be {expected_p_value}, but got {p_value}."

# Run the tests
if __name__ == "__main__":
    pytest.main()