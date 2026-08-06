import pandas as pd
import seaborn as sns
import pytest

def task_func(df, col1, col2):
    if not isinstance(df, pd.DataFrame) or df.empty or col1 not in df.columns or col2 not in df.columns:
        raise ValueError("The DataFrame is empty or the specified column does not exist.")
    
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax

def test_task_func():
    # Test case 1: df is not a DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func("not_a_df", "col1", "col2")
    assert "The DataFrame is empty or the specified column does not exist." in str(excinfo.value)

    # Test case 2: df is empty
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df, "col1", "col2")
    assert "The DataFrame is empty or the specified column does not exist." in str(excinfo.value)

    # Test case 3: col1 does not exist in df
    df = pd.DataFrame({"col3": [1, 2, 3]})
    with pytest.raises(ValueError) as excinfo:
        task_func(df, "col1", "col2")
    assert "The DataFrame is empty or the specified column does not exist." in str(excinfo.value)

    # Test case 4: col2 does not exist in df
    df = pd.DataFrame({"col1": [1, 2, 3]})
    with pytest.raises(ValueError) as excinfo:
        task_func(df, "col1", "col2")
    assert "The DataFrame is empty or the specified column does not exist." in str(excinfo.value)

    # Test case 5: df is a DataFrame, col1 and col2 exist, and the function returns an Axes object
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    ax = task_func(df, "col1", "col2")
    assert isinstance(ax, sns.axisgrid.Axes)