import pytest
from src_0921 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }

def test_task_func(sample_data):
    ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    assert ax.get_title() == 'Correlation Matrix', "The title of the heatmap should be 'Correlation Matrix'"
    
    # Check if the heatmap is annotated
    texts = ax.texts
    assert len(texts) > 0, "The heatmap should be annotated with correlation values"

    # Check if the dataframe is correctly converted and correlation matrix is calculated
    df = pd.DataFrame(sample_data)
    expected_corr = df.corr()
    actual_corr = pd.DataFrame([[float(t.get_text()) for t in row] for row in ax.collections[0].get_offsets().reshape(-1, len(df.columns))])
    pd.testing.assert_frame_equal(expected_corr, actual_corr, check_less_precise=2)

# To run the tests, you can use the following command in your terminal:
# pytest -v