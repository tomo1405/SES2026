import pytest
from src_0065 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    return [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 5],
        [2, 1, 6],
        [2, 1, 7],
        [3, 2, 8]
    ]

def test_task_func(sample_data):
    analyzed_df, ax = task_func(sample_data)
    
    # Check if the DataFrame is correctly pivoted
    expected_df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': [2, 1, 2],
        'col3': [2, 2, 1]
    }).set_index(['col1', 'col2']).unstack(fill_value=0)
    
    pd.testing.assert_frame_equal(analyzed_df, expected_df)

    # Check if the axes object is of the correct type
    assert isinstance(ax, sns.axisgrid.FacetGrid)