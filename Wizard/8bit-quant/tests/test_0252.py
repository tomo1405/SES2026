python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")

    job_count = data['Job'].value_counts()
    
    labels = job_count.index.tolist()
    sizes = job_count.values.tolist()
    colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]
        
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')

    return fig

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'Job': ['Manager', 'Developer', 'Developer', 'Manager', 'Developer']})
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

    # Test case 2: Invalid input
    with pytest.raises(ValueError):
        task_func(123)