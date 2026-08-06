import pytest
from src_0301 import task_func
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    return pd.DataFrame(data)

def test_task_func_output(sample_data):
    result_df, result_fig = task_func(sample_data)
    
    # Check if the DataFrame is correctly transformed
    assert 'Date' in result_df.columns, "DataFrame should have a 'Date' column"
    assert all(isinstance(d, pd.Timestamp) for d in result_df['Date']), "All dates should be converted to Timestamp"
    assert result_df.shape == (3, 3), "DataFrame should have 3 rows and 3 columns"
    
    # Check if the Z-scores are calculated correctly
    expected_zscores = np.array([
        [-1.22474487, -1.22474487],
        [0., 0.],
        [1.22474487, 1.22474487]
    ])
    np.testing.assert_almost_equal(result_df.iloc[:, 1:].values, expected_zscores, decimal=6, err_msg="Z-scores calculation is incorrect")
    
    # Check if the figure is created
    assert isinstance(result_fig, plt.Figure), "Result should be a matplotlib Figure object"

def test_task_func_plot(sample_data, monkeypatch):
    # Capture the plot output
    buf = io.BytesIO()
    monkeypatch.setattr(plt, 'show', lambda: buf.write(b'Plot Data'))
    
    _, _ = task_func(sample_data)
    
    buf.seek(0)
    plot_data = buf.read()
    assert plot_data == b'Plot Data', "Plot was not displayed correctly"