import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src_0303 import task_func
import pytest

# Constants
COLUMNS = ['Date', 'Value']

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(None)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(columns=COLUMNS))
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(columns=COLUMNS).reindex(columns=['Date']))
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(columns=COLUMNS).reindex(index=[]))

def test_task_func_valid_input():
    df = pd.DataFrame(columns=COLUMNS)
    df['Date'] = pd.date_range(start='2023-01-01', periods=3)
    df['Value'] = [1, 2, 3]
    corr_df, heatmap = task_func(df, plot=True)
    assert isinstance(corr_df, pd.DataFrame)
    assert isinstance(heatmap, plt.Axes)