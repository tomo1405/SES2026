import pytest
from src_0917 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func():
    df = pd.DataFrame({'closing_price': [10, 20, 30, 40, 50]})
    boxplot_ax, histplot_ax = task_func(df)
    
    assert isinstance(boxplot_ax, plt.Axes)
    assert isinstance(histplot_ax, plt.Axes)
    
    assert boxplot_ax.get_title() == 'Box Plot of Closing Prices'
    assert histplot_ax.get_title() == 'Histogram of Closing Prices'
    
    assert len(boxplot_ax.get_xticklabels()) == 5
    assert len(histplot_ax.get_xticklabels()) == 5
    
    assert boxplot_ax.get_xlabel() == 'Closing Price'
    assert histplot_ax.get_xlabel() == 'Closing Price'
    
    assert boxplot_ax.get_ylabel() == 'Count'
    assert histplot_ax.get_ylabel() == 'Density'
    
    assert boxplot_ax.get_yticklabels() == ['10', '20', '30', '40', '50']
    assert histplot_ax.get_yticklabels() == ['10', '20', '30', '40', '50']