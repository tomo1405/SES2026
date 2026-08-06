import pytest
from src_0433 import task_func
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Mock data for testing
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature1': ['A', 'B', 'A', 'B']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature2': ['X', 'Y', 'X', 'Z']
})

def test_task_func():
    p_value, heatmap = task_func(df1, df2)
    
    # Check if p_value is a float
    assert isinstance(p_value, float)
    
    # Check if heatmap is a seaborn.axisgrid.AxesGrid object
    assert isinstance(heatmap, sns.axisgrid.AxesGrid)
    
    # Check if the heatmap figure has been created
    assert plt.fignum_exists(1)

    # Clean up the plot
    plt.close()