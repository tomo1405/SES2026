python
import pandas as pd
import seaborn as sns
import numpy as np
import ast
import pytest

def task_func(csv_file):
    df = pd.read_csv(csv_file)
    df['list'] = df['list'].map(ast.literal_eval)
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['std'] = df['list'].apply(np.std)
    plot = sns.histplot(df['mean'], kde=True)
    return df, plot

def test_task_func():
    # Test case 1: Test if the function returns a dataframe and a plot object
    df, plot = task_func('test_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.axisgrid.FacetGrid)

    # Test case 2: Test if the function returns the correct values for the mean, sum, and std columns
    df, plot = task_func('test_data.csv')
    assert df['mean'][0] == 2.5
    assert df['sum'][0] == 10
    assert df['std'][0] == 0.7071067811865476

    # Test case 3: Test if the function returns the correct number of rows and columns in the dataframe
    df, plot = task_func('test_data.csv')
    assert df.shape == (2, 5)

    # Test case 4: Test if the function returns the correct number of rows and columns in the plot object
    df, plot = task_func('test_data.csv')
    assert plot.axes.shape == (1, 1)
    assert plot.axes[0, 0].get_xlabel() == 'Mean'
    assert plot.axes[0, 0].get_ylabel() == 'Density'