python
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
    df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
    with pytest.raises(ValueError):
        task_func('not a dataframe')
    ax = task_func(df)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Value Distribution'