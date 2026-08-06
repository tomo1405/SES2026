import pytest
from src_0069 import task_func
import pandas as pd
import seaborn as sns
from io import StringIO

# Mock data for testing
mock_data = """Employee ID,Age
EMP123,30
EMP456,25
EMP789,35"""

@pytest.fixture
def mock_csv_file(monkeypatch):
    def mock_read_csv(filepath_or_buffer, *args, **kwargs):
        if filepath_or_buffer == '/path/to/data.csv':
            return pd.read_csv(StringIO(mock_data))
        return pd.read_csv(filepath_or_buffer, *args, **kwargs)

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func(mock_csv_file):
    df, ax = task_func('/path/to/data.csv', 'EMP')
    
    # Check DataFrame
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert 'Employee ID' in df.columns
    assert 'Age' in df.columns
    assert all(df['Employee ID'].str.startswith('EMP'))

    # Check Seaborn Axes object
    assert isinstance(ax, sns.axisgrid.FacetGrid)

    # Check plot properties (basic check)
    assert 'Age' in ax.data.columns
    assert ax._x_var == 'Age'
    assert ax._legend_data is not None