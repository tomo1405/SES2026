python
import pandas as pd
import numpy as np
import pytest
from src_0301 import task_func

def test_task_func():
    # Test case 1: Test if the function returns a dataframe and a figure object
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': [10, 20, 30]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)
    
    # Test case 2: Test if the function returns a dataframe with z-scores
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': [10, 20, 30]})
    df, fig = task_func(df)
    assert np.allclose(df.iloc[:,1:], np.array([[-1.34164079, -1.34164079], [-0.4472136, -0.4472136], [0.4472136, 0.4472136]]))
    
    # Test case 3: Test if the function returns a figure with a title and x and y labels
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': [10, 20, 30]})
    df, fig = task_func(df)
    assert fig.axes[0].get_title() == 'Z-Scores Over Time'
    assert fig.axes[0].get_xlabel() == 'Date'
    assert fig.axes[0].get_ylabel() == 'Z-Score'