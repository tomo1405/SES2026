import pytest
from src_0430 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mock data for testing
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'feature1': [10, 20, 30],
    'feature2': [15, 25, 35],
    'target': [0, 1, 0]
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'feature3': [100, 200, 300]
})

def test_task_func():
    selected_features, heatmap = task_func(df1, df2)
    
    # Check if the selected features are correct
    assert selected_features == ['feature1', 'feature2'], "The selected features are incorrect"
    
    # Check if the heatmap is a matplotlib Axes object
    assert isinstance(heatmap, plt.Axes), "The heatmap is not a matplotlib Axes object"

    # Check if the heatmap data is correct
    corr_matrix = pd.DataFrame({
        'feature1': [1.0, 0.9],
        'feature2': [0.9, 1.0]
    }, index=['feature1', 'feature2'])
    assert heatmap.get_figure().get_axes()[0].get_title() == '', "Heatmap title should be empty"
    assert heatmap.get_figure().get_axes()[0].get_xlabel() == '', "Heatmap xlabel should be empty"
    assert heatmap.get_figure().get_axes()[0].get_ylabel() == '', "Heatmap ylabel should be empty"
    assert heatmap.get_figure().get_axes()[0].get_images()[0].get_array().shape == corr_matrix.shape, "Heatmap data shape is incorrect"
    np.testing.assert_allclose(heatmap.get_figure().get_axes()[0].get_images()[0].get_array(), corr_matrix.values, rtol=1e-05, atol=1e-08)

# Run the tests
if __name__ == "__main__":
    pytest.main()