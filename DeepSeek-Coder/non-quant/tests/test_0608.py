import pytest
from src_0608 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

# Mock data for testing
@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 3, 2, 5, 4],
        'D': [4, 3, 2, 1, 5],
        'E': [5, 1, 4, 3, 2]
    }
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    df = sample_data
    tuples = [(1, 5), (2, 4)]
    n_plots = 2
    result_df, plots = task_func(df, tuples, n_plots=n_plots)

    assert isinstance(result_df, pd.DataFrame)
    assert len(plots) == n_plots
    assert all(isinstance(plot, plt.Axes) for plot in plots)