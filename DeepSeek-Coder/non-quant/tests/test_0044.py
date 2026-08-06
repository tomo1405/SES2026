import pytest
from src_0044 import task_func
import numpy as np
import seaborn as sns
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 2, 2, 2, 2]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    description, plots = task_func(sample_data)
    assert isinstance(description, pd.core.frame.DataFrame)
    assert len(plots) == 2  # Assuming 2 numerical columns based on the data
    assert all(isinstance(plot, plt.Axes) for plot in plots)