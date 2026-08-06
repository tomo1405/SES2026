python
import numpy as np
import pandas as pd
import pytest

def task_func(array_length=100):
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)

    statistics = {
        'Array1': [np.mean(array1), np.median(array1), np.std(array1)],
        'Array2': [np.mean(array2), np.median(array2), np.std(array2)]
    }

    df = pd.DataFrame(statistics, index=['Mean', 'Median', 'Standard Deviation'])
    ax = df.plot(kind='bar')

    return df, ax

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)