import pytest
from src_0036 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 3, 2, 4, 5]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    result_df, _ = task_func(df)
    assert result_df.equals(df)

def test_plot(sample_data):
    df = sample_data
    _, ax = task_func(df)
    assert ax is not None
    plt.close()