import pytest
from src_0917 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'closing_price': [100, 102, 101, 98, 97, 105, 110, 108, 107, 103]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    boxplot_ax, histplot_ax = task_func(sample_df)
    
    assert isinstance(boxplot_ax, sns.axisgrid.AxesSubplot), "The first returned object should be a seaborn AxesSubplot for the box plot."
    assert isinstance(histplot_ax, sns.axisgrid.FacetGrid), "The second returned object should be a seaborn FacetGrid for the histogram."
    
    # Check that the titles are set correctly
    assert boxplot_ax.get_title() == 'Box Plot of Closing Prices', "The box plot should have the correct title."
    assert histplot_ax.axes[0].get_title() == 'Histogram of Closing Prices', "The histogram should have the correct title."
    
    # Check that the data is plotted correctly
    assert len(boxplot_ax.collections) > 0, "The box plot should contain data."
    assert len(histplot_ax.ax.patches) > 0, "The histogram should contain data."

    # Check that the figure is closed
    with pytest.raises(AttributeError):
        boxplot_ax.figure.canvas.draw_idle()