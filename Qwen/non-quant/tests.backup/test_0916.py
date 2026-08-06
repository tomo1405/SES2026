import pytest
from src_0916 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'closing_price': [100, 102, 101, 105, 110, 108, 107, 103, 104, 106]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    outliers, ax = task_func(sample_df)
    
    # Check if the outliers DataFrame is correctly identified
    expected_outliers = sample_df.iloc[[4, 5]]
    pd.testing.assert_frame_equal(outliers.reset_index(drop=True), expected_outliers.reset_index(drop=True))
    
    # Check if the plot is created with the correct properties
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Closing Price'
    assert ax.get_title() == 'Outliers in Closing Prices'
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert 'Normal' in legend_labels
    assert 'Outlier' in legend_labels
    
    # Close the plot to avoid displaying it during testing
    plt.close(fig=ax.get_figure())