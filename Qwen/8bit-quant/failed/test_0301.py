import pytest
from src_0301 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
        'Value': [[1, 2], [3, 4], [5, 6]]
    }
    return pd.DataFrame(data)

def test_task_func_output(sample_data):
    df, fig = task_func(sample_data)
    
    # Check if the DataFrame has been transformed correctly
    assert 'Date' in df.columns
    assert all(isinstance(date, pd.Timestamp) for date in df['Date'])
    assert df.shape == (3, 3)  # 3 rows and 3 columns (Date + 2 values)
    
    # Check if the z-score transformation is applied
    z_scores = df.iloc[:, 1:]
    assert z_scores.applymap(lambda x: isinstance(x, float)).all().all(), "All elements should be floats"
    
    # Check if the plot is created
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue(), "The plot should not be empty"

def test_task_func_plot_title(sample_data):
    _, fig = task_func(sample_data)
    ax = fig.axes[0]
    assert ax.get_title() == 'Z-Scores Over Time', "The plot title is incorrect"

def test_task_func_plot_labels(sample_data):
    _, fig = task_func(sample_data)
    ax = fig.axes[0]
    assert ax.get_xlabel() == 'Date', "The x-axis label is incorrect"
    assert ax.get_ylabel() == 'Z-Score', "The y-axis label is incorrect"