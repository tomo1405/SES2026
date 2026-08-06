import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    value_counts = df['value'].value_counts()
    ax = plt.bar(value_counts.index, value_counts.values)
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Value Distribution')
    return plt.gca()

def test_task_func():
    # Test case 1: input is a DataFrame
    df = pd.DataFrame({'value': [1, 2, 3, 1, 2]})
    result = task_func(df)
    assert isinstance(result, plt.Axes)
    
    # Test case 2: input is not a DataFrame
    with pytest.raises(ValueError):
        task_func([1, 2, 3])
    
    # Test case 3: input is a DataFrame with missing values
    df = pd.DataFrame({'value': [1, 2, None, 1, 2]})
    result = task_func(df)
    assert isinstance(result, plt.Axes)