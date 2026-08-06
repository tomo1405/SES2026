python
import pandas as pd
import seaborn as sns
import pytest

def task_func(df, col1, col2):
    # Ensure that the df is DataFrame, not empty and the specified column exists
    if not isinstance(df, pd.DataFrame) or df.empty or col1 not in df.columns or col2 not in df.columns:
        raise ValueError("The DataFrame is empty or the specified column does not exist.")
    
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    col1 = 'col1'
    col2 = 'col2'
    ax = task_func(df, col1, col2)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

    # Test case 2: Invalid input - df is empty
    df = pd.DataFrame()
    col1 = 'col1'
    col2 = 'col2'
    with pytest.raises(ValueError):
        task_func(df, col1, col2)

    # Test case 3: Invalid input - col1 does not exist
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    col1 = 'col3'
    col2 = 'col2'
    with pytest.raises(ValueError):
        task_func(df, col1, col2)

    # Test case 4: Invalid input - col2 does not exist
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    col1 = 'col1'
    col2 = 'col3'
    with pytest.raises(ValueError):
        task_func(df, col1, col2)