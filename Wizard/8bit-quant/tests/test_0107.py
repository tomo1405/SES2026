python
import pandas as pd
import pytest
from src_0107 import task_func

def test_task_func():
    # Test case 1: valid input
    df = pd.DataFrame({'group': ['A', 'B', 'A', 'B'],
                       'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
                       'value': [10, 20, 30, 40]})
    model, y_pred, ax = task_func(df)
    assert isinstance(model, LinearRegression)
    assert isinstance(y_pred, pd.Series)
    assert isinstance(ax, plt.Axes)

    # Test case 2: invalid input (missing column)
    df = pd.DataFrame({'group': ['A', 'B', 'A', 'B'],
                       'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
                       'value': [10, 20, 30, 40]})
    with pytest.raises(ValueError):
        task_func(df[['group', 'date']])

    # Test case 3: invalid input (invalid column type)
    df = pd.DataFrame({'group': ['A', 'B', 'A', 'B'],
                       'date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
                       'value': [10, 20, 30, 40]})
    df['date'] = ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04']
    with pytest.raises(ValueError):
        task_func(df)