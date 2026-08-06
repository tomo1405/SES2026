import pandas as pd
from src_0433 import task_func


def test_task_func():
    # Mock input dataframes
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [7, 8, 9]})

    # Call the function and store the returned values
    p_value, heatmap = task_func(df1, df2)

    # Define the expected output
    expected_p_value = 0.01
    expected_heatmap = ...  # Define the expected heatmap output

    # Assert that the function returned the expected values
    assert p_value == expected_p_value
    assert heatmap == expected_heatmap