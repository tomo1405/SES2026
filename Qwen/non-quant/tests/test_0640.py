import pytest
from src_0640 import task_func
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func_output():
    df, ax = task_func(num_samples=5, num_features=3)
    
    # Check DataFrame shape
    assert df.shape == (5, 3), "DataFrame shape is incorrect"
    
    # Check DataFrame index and columns
    expected_index = ['Sample1', 'Sample2', 'Sample3', 'Sample4', 'Sample5']
    expected_columns = ['Feature1', 'Feature2', 'Feature3']
    assert list(df.index) == expected_index, "DataFrame index is incorrect"
    assert list(df.columns) == expected_columns, "DataFrame columns are incorrect"
    
    # Check that the DataFrame contains only float values
    assert df.dtypes.apply(lambda x: pd.api.types.is_float_dtype(x)).all(), "DataFrame contains non-float values"
    
    # Check the heatmap axes
    assert isinstance(ax, sns.axisgrid.AxesGrid), "Returned object is not a Seaborn AxesGrid"
    
    # Check that the heatmap is annotated
    text = [t.get_text() for t in ax.texts]
    assert len(text) > 0, "Heatmap is not annotated"
    
    # Close the plot to prevent it from displaying during tests
    plt.close(ax.figure)

def test_task_func_default_parameters():
    df, ax = task_func()
    
    # Check default parameters
    assert df.shape == (100, 5), "Default DataFrame shape is incorrect"
    
    # Close the plot
    plt.close(ax.figure)