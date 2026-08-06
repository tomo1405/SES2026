import pytest
from src_0662 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    x = [
        np.array([1, 2, 3]),
        np.array([4, 5, 6]),
        np.array([7, 8, 9]),
        np.array([10, 11, 12]),
        np.array([13, 14, 15])
    ]
    y = [
        np.array([16, 17, 18]),
        np.array([19, 20, 21]),
        np.array([22, 23, 24]),
        np.array([25, 26, 27]),
        np.array([28, 29, 30])
    ]
    labels = ['H₂O', 'O₂', 'CO₂', 'N₂', 'Ar']
    return x, y, labels

def test_task_func(sample_data):
    x, y, labels = sample_data
    ax, df = task_func(x, y, labels)
    
    # Check if the DataFrame is created correctly
    expected_data = {
        'H₂O': [1, 2, 3, 16, 17, 18],
        'O₂': [4, 5, 6, 19, 20, 21],
        'CO₂': [7, 8, 9, 22, 23, 24],
        'N₂': [10, 11, 12, 25, 26, 27],
        'Ar': [13, 14, 15, 28, 29, 30]
    }
    expected_df = pd.DataFrame(expected_data, index=range(6))
    pd.testing.assert_frame_equal(df, expected_df)

    # Check if the heatmap axis object is created
    assert isinstance(ax, sns.axisgrid.FacetGrid)