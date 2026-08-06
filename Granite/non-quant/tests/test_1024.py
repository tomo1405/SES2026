from unittest.mock import patch

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest


def task_func(dataframe):
    if dataframe.empty:
        raise ValueError("DataFrame is empty.")
        
    if not all(dataframe.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise TypeError("All columns must be numeric for correlation calculation.")

    if dataframe.shape[1] < 2:
        raise ValueError("DataFrame must have at least two columns for correlation calculation.")

    # Explicit use of pd.DataFrame.corr() to calculate the correlation matrix
    corr_matrix = pd.DataFrame.corr(dataframe)
    abs_corr_matrix = corr_matrix.abs()

    # Finding the pair of columns with the highest absolute correlation
    highest_corr_value = abs_corr_matrix.unstack().dropna().nlargest(2).iloc[-1]
    max_corr_pair = np.where(abs_corr_matrix == highest_corr_value)

    # Extracting column names for the highest correlation
    column_x = dataframe.columns[max_corr_pair[0][0]]
    column_y = dataframe.columns[max_corr_pair[1][0]]

    # Using plt to plot the scatter plot
    plt.figure(figsize=(10, 6))  # Creating a figure
    plt.scatter(dataframe[column_x], dataframe[column_y])  # Plotting the scatter plot
    plt.title(f"Scatter plot between {column_x} and {column_y}")  # Setting the title
    plt.xlabel(column_x)  # Setting the x-axis label
    plt.ylabel(column_y)  # Setting the y-axis label
    plt.show()  # Displaying the figure

    return plt.gca()  # Returning the current Axes object for further use

def test_task_func():
    # Test case 1: DataFrame is empty
    dataframe = pd.DataFrame()
    with patch('matplotlib.pyplot.show') as mock_show:
        with pytest.raises(ValueError, match="DataFrame is empty."):
            task_func(dataframe)
    mock_show.assert_not_called()

    # Test case 2: All columns are not numeric
    dataframe = pd.DataFrame({
        'column1': ['a', 'b', 'c'],
        'column2': [1, 2, 3]
    })
    with patch('matplotlib.pyplot.show') as mock_show:
        with pytest.raises(TypeError, match="All columns must be numeric for correlation calculation."):
            task_func(dataframe)
    mock_show.assert_not_called()

    # Test case 3: DataFrame has less than two columns
    dataframe = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': [4, 5, 6]
    })
    with patch('matplotlib.pyplot.show') as mock_show:
        with pytest.raises(ValueError, match="DataFrame must have at least two columns for correlation calculation."):
            task_func(dataframe)
    mock_show.assert_not_called()

    # Test case 4: DataFrame has two numeric columns
    dataframe = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': [4, 5, 6]
    })
    with patch('matplotlib.pyplot.show') as mock_show:
        with patch('matplotlib.pyplot.gca') as mock_gca:
            task_func(dataframe)
    mock_show.assert_called_once()
    mock_gca.assert_called_once()