python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def task_func(df: pd.DataFrame) -> tuple:
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    boxplot_ax = sns.boxplot(x=df['closing_price'], ax=axes[0])
    boxplot_ax.set_title('Box Plot of Closing Prices')
    
    histplot_ax = sns.histplot(df['closing_price'], kde=True, ax=axes[1])
    histplot_ax.set_title('Histogram of Closing Prices')
    
    plt.tight_layout()
    plt.close(fig)  # Prevent automatic figure display within Jupyter notebooks or interactive environments.
    
    return boxplot_ax, histplot_ax

def test_task_func():
    df = pd.DataFrame({'closing_price': [10, 20, 30, 40, 50]})
    boxplot_ax, histplot_ax = task_func(df)
    
    assert isinstance(boxplot_ax, sns.axisgrid.FacetGrid)
    assert isinstance(histplot_ax, sns.axisgrid.FacetGrid)
    assert boxplot_ax.axes[0][0].get_title() == 'Box Plot of Closing Prices'
    assert histplot_ax.axes[0][0].get_title() == 'Histogram of Closing Prices'