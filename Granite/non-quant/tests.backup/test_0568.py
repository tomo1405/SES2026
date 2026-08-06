import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch

def task_func(data):
    data = data.split('-')
    data = [int(d) for d in data]
    df = pd.DataFrame(data, columns=['Values'])
    
    plt.figure(figsize=(10, 6))
    ax = plt.gca()  # Get current Axes
    ax.hist(df['Values'], bins=np.arange(df['Values'].min(), df['Values'].max()+2) - 0.5, edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    ax.set_xticks(sorted(list(set(data))))  # Set x-ticks based on unique data values
    plt.show()
    
    return ax

def test_task_func():
    data = "1-2-3-4-5"
    ax = task_func(data)
    assert ax is not None
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Histogram of Values'
    assert ax.get_xticks().tolist() == [1, 2, 3, 4, 5]

def test_task_func_with_mock():
    with patch('matplotlib.pyplot.show') as mock_show:
        data = "1-2-3-4-5"
        ax = task_func(data)
        mock_show.assert_called_once()