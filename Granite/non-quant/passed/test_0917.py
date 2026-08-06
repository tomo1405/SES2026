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
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'closing_price': [100, 200, 300, 400, 500]
    })
    
    # Call the function and store the returned values
    boxplot_ax, histplot_ax = task_func(df)
    
    # Perform assertions to test the function's behavior
    assert isinstance(boxplot_ax, plt.Axes)
    assert isinstance(histplot_ax, plt.Axes)
    assert boxplot_ax.get_title() == 'Box Plot of Closing Prices'
    assert histplot_ax.get_title() == 'Histogram of Closing Prices'

if __name__ == '__main__':
    pytest.main()