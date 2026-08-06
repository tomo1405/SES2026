import pandas as pd
import seaborn as sns
import pytest

def task_func(df, col1, col2):
    if not isinstance(df, pd.DataFrame) or df.empty or col1 not in df.columns or col2 not in df.columns:
        raise ValueError("The DataFrame is empty or the specified column does not exist.")
    
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax

def test_task_func():
    # Test case 1: Ensure that the df is DataFrame, not empty and the specified column exists
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    col1 = 'col1'
    col2 = 'col2'
    ax = task_func(df, col1, col2)
    assert isinstance(ax, sns.axisgrid.RegPlot)

    # Test case 2: The DataFrame is empty
    df = pd.DataFrame()
    col1 = 'col1'
    col2 = 'col2'
    with pytest.raises(ValueError) as e:
        task_func(df, col1, col2)
    assert str(e.value) == "The DataFrame is empty or the specified column does not exist."

    # Test case 3: The specified column does not exist
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    col1 = 'col3'
    col2 = 'col2'
    with pytest.raises(ValueError) as e:
        task_func(df, col1, col2)
    assert str(e.value) == "The DataFrame is empty or the specified column does not exist."