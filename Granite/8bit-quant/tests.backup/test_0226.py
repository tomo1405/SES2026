import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df, dct, columns=None, plot_histograms=False):
    
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    # Replace values using dictionary mapping
    df_replaced = df.replace(dct)
    
    # Plot a histogram for each specified column
    if plot_histograms and columns:
        for column in columns:
            if column in df_replaced:
                df_replaced[column].plot.hist(bins=50)
                plt.title(column)

    return df_replaced

# Define a sample DataFrame and dictionary for testing
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
dct = {'A': 10, 'B': 20}

# Test the function with valid input
def test_task_func_valid_input():
    result = task_func(df, dct, columns=['A', 'B'], plot_histograms=True)
    assert isinstance(result, pd.DataFrame)
    assert 'A' in result.columns and 'B' in result.columns
    assert len(result) == 3

# Test the function with invalid input
def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func('not_a_df', dct)

# Test the function with plot_histograms=False
def test_task_func_no_plot():
    result = task_func(df, dct, columns=['A', 'B'], plot_histograms=False)
    assert isinstance(result, pd.DataFrame)
    assert 'A' in result.columns and 'B' in result.columns
    assert len(result) == 3