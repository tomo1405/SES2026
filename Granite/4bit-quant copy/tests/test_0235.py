import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    df = df.drop_duplicates(subset='Name')

    slope, intercept, r_value, _, _ = stats.linregress(df['Age'], df['Score'])

    df['Age_up'] = intercept + slope * df['Age']
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    plt.scatter(df['Age'], df['Score'], label='Data')
    plt.plot(df['Age'].values, df['Age_up'].values, 'r', label='Fitted line')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.title('Linear Regression')
    plt.legend()
    return plt, ax

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [20, 25, 30], 'Score': [80, 90, 95]})
    plt, ax = task_func(df)
    assert isinstance(plt, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert plt.fignum == 1
    assert ax.get_geometry() == (1, 1, 1)
    assert ax.get_xlabel() == 'Age'
    assert ax.get_ylabel() == 'Score'
    assert ax.get_title() == 'Linear Regression'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_label() == 'Data'
    assert ax.get_lines()[1].get_label() == 'Fitted line'

def test_task_func_invalid_input():
    with pytest.raises(ValueError, match="The input df is not a DataFrame"):
        task_func("invalid input")