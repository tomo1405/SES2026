import pytest
from src_0072 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_csv(tmp_path):
    data = {
        'list': ['[1, 2, 3]', '[4, 5, 6]', '[7, 8, 9]']
    }
    df = pd.DataFrame(data)
    csv_file = tmp_path / "sample.csv"
    df.to_csv(csv_file, index=False)
    return csv_file

def test_task_func(sample_csv):
    df, plot = task_func(str(sample_csv))
    
    # Check if the DataFrame is correctly processed
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'std' in df.columns
    
    # Check if the sums are calculated correctly
    expected_sums = [6, 15, 24]
    assert all(df['sum'] == expected_sums)
    
    # Check if the means are calculated correctly
    expected_means = [2, 5, 8]
    assert all(df['mean'] == expected_means)
    
    # Check if the standard deviations are calculated correctly
    expected_stds = [np.sqrt(2/3), np.sqrt(2/3), np.sqrt(2/3)]
    assert all(np.isclose(df['std'], expected_stds))
    
    # Check if the plot is a matplotlib Axes object
    assert isinstance(plot, plt.Axes)

    # Close the plot to prevent it from displaying during tests
    plt.close(plot)