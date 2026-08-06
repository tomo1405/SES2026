import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

from src_0917 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'closing_price': [100, 200, 300, 400, 500]
    })

def test_task_func(sample_df):
    boxplot_ax, histplot_ax = task_func(sample_df)
    
    assert isinstance(boxplot_ax, plt.Axes)
    assert isinstance(histplot_ax, plt.Axes)
    
    assert boxplot_ax.get_title() == 'Box Plot of Closing Prices'
    assert histplot_ax.get_title() == 'Histogram of Closing Prices'

def test_task_func_with_invalid_input(sample_df):
    with pytest.raises(TypeError):
        task_func('invalid_input')