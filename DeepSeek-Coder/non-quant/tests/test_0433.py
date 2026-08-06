import pytest
from src_0433 import task_func
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency

def test_task_func():
    # Create sample dataframes for testing
    data1 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': ['A', 'B', 'C'],
        'feature2': ['X', 'Y', 'Z']
    })
    data2 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': ['A', 'B', 'C'],
        'feature2': ['X', 'Y', 'Z']
    })

    # Call the function with the sample data
    result = task_func(data1, data2)

    # Add assertions to validate the output
    assert isinstance(result, tuple), "The function should return a tuple"
    assert len(result) == 2, "The function should return a tuple with two elements"
    assert isinstance(result[0], float), "The first element of the tuple should be a float"
    assert isinstance(result[1], sns.axisgrid.HeatMap), "The second element of the tuple should be a heatmap"