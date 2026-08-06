import pandas as pd
import pytest
import seaborn as sns
from src_0067 import task_func


@pytest.fixture
def sample_data():
    return [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 5],
        [2, 2, 6],
        [2, 3, 7]
    ]

def test_task_func_output(sample_data):
    analyzed_df, ax = task_func(sample_data)
    
    # Check if the DataFrame is correctly grouped and counted
    expected_df = pd.DataFrame({
        'col1': [1, 1, 2],
        'col2': [2, 3, 2],
        'col3': [2, 1, 1]
    })
    pd.testing.assert_frame_equal(analyzed_df.reset_index(drop=True), expected_df)

    # Check if the seaborn axis object is created
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_empty_data():
    data = []
    analyzed_df, ax = task_func(data)
    
    # Check if the DataFrame is empty
    assert analyzed_df.empty
    
    # Check if the seaborn axis object is created
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_single_row_data():
    data = [[1, 2, 3]]
    analyzed_df, ax = task_func(data)
    
    # Check if the DataFrame is correctly grouped and counted
    expected_df = pd.DataFrame({
        'col1': [1],
        'col2': [2],
        'col3': [1]
    })
    pd.testing.assert_frame_equal(analyzed_df.reset_index(drop=True), expected_df)
    
    # Check if the seaborn axis object is created
    assert isinstance(ax, sns.axisgrid.FacetGrid)