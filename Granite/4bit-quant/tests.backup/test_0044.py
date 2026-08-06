import pytest
import numpy as np
import seaborn as sns

def task_func(df):
    df = df.fillna(df.mean(axis=0))
    description = df.describe()
    plots = []
    for col in df.select_dtypes(include=[np.number]).columns:
        plot = sns.displot(df[col], bins=10)
        plots.append(plot.ax)
    return description, plots

def test_task_func():
    # Mock the input dataframe
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 20, 30, 40, 50]
    })

    # Call the function
    description, plots = task_func(df)

    # Assert the expected output
    assert description.loc['mean']['A'] == 3
    assert len(plots) == 2