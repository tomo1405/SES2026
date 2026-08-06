import pytest
from src_0103 import task_func
import matplotlib.pyplot as plt
import pandas as pd

def test_task_func():
    fig, df = task_func()
    
    # Check if the returned figure is an instance of plt.Figure
    assert isinstance(fig, plt.Figure), "The returned figure is not an instance of plt.Figure"
    
    # Check if the returned DataFrame is an instance of pd.DataFrame
    assert isinstance(df, pd.DataFrame), "The returned DataFrame is not an instance of pd.DataFrame"
    
    # Check if the DataFrame has the correct number of columns
    expected_columns = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
    assert list(df.columns) == expected_columns, f"DataFrame columns do not match expected: {expected_columns}"
    
    # Check if the DataFrame has the correct number of rows (should be 442 for diabetes dataset)
    assert len(df) == 442, "DataFrame does not have the expected number of rows"