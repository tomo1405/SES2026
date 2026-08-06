import pytest
from src_0917 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@pytest.fixture
def sample_df():
    data = {
        'closing_price': [100, 102, 101, 98, 97, 105, 103, 104, 106, 107]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    boxplot_ax, histplot_ax = task_func(sample_df)
    
    # Check if the returned objects are AxesSubplot instances
    assert isinstance(boxplot_ax, plt.Axes)
    assert isinstance(histplot_ax, plt.Axes)
    
    # Check if the titles are set correctly
    assert boxplot_ax.get_title() == 'Box Plot of Closing Prices'
    assert histplot_ax.get_title() == 'Histogram of Closing Prices'
    
    # Check if the plots contain the correct data
    boxplot_data = boxplot_ax.collections[0].get_offsets().data
    histplot_data, _ = histplot_ax.get_lines()[0].get_data()
    
    assert all(boxplot_data[:, 0] == sample_df['closing_price'].values)
    assert all(histplot_data == sample_df['closing_price'].values)