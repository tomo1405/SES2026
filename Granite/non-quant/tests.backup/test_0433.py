import pytest
from src_0433 import task_func

def test_task_func():
    # Mock input dataframes
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": [4, 5, 6]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": [7, 8, 9]})
    
    # Call the function with the mock dataframes
    p, heatmap = task_func(df1, df2)
    
    # Assert the expected output types and values
    assert isinstance(p, float)
    assert 0 <= p <= 1
    assert isinstance(heatmap, sns.matrix.DataFrameHeatmap)