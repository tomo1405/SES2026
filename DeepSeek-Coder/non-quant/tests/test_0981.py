import pytest
from src_0981 import task_func
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    result, fig = task_func(df)
    
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert isinstance(fig, plt.Figure), "The figure should be a matplotlib figure"
    assert len(fig.axes) == 1, "There should be one subplot"
    assert len(fig.axes[0].patches) == 3, "The heatmap should have 3 cells"