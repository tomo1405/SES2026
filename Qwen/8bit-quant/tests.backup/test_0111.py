import pytest
from src_0111 import task_func
import pandas as pd
import io
import sys

def test_task_func_invalid_input_type():
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns."):
        task_func([1, 2, 3])

def test_task_func_missing_columns():
    df = pd.DataFrame({'Date': ['2023-01-01'], 'Revenue': [100]})
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns."):
        task_func(df)

def test_task_func_empty_resampled_data():
    df = pd.DataFrame({'Date': ['2023-01-01'], 'Sales': [0]})
    with pytest.raises(ValueError, match="No data available to plot after resampling."):
        task_func(df)

def test_task_func_valid_data(capsys):
    df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Sales': [100, 200, 300]
    })
    
    # Redirect stdout to capture the plot output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    ax = task_func(df)
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Daily Turnover'
    assert ax.get_ylabel() == 'Sales'
    assert captured_output.getvalue() == ''  # No print statements expected

# Note: The actual plot display (plt.show()) is not tested here as it would require a GUI environment.
# Instead, we check that the function returns a matplotlib Axes object and sets the correct title and labels.