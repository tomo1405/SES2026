import pytest
from src_0069 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# Mock data for testing
mock_data = """Employee ID,Age
EMP123,30
EMP456,25
EMP789,35"""

@pytest.fixture
def mock_file(monkeypatch):
    def mock_read_csv(filepath_or_buffer, *args, **kwargs):
        return pd.read_csv(StringIO(mock_data), *args, **kwargs)
    
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func(mock_file):
    df, ax = task_func(data=StringIO(mock_data), emp_prefix='EMP')
    
    # Check if the DataFrame is filtered correctly
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert all(df['Employee ID'].str.startswith('EMP'))
    
    # Check if the plot is created correctly
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert ax._x_var == 'Age'
    assert ax._legend_data['kde'] is not None
    
    # Close the plot to avoid warnings
    plt.close(ax.fig)