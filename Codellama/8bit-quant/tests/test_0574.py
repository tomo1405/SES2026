import matplotlib
import numpy as np
import pandas as pd
from src_0574 import task_func


def test_task_func():
    array_length = 100
    df, ax = task_func(array_length)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

    assert df.shape == (3, 2)
    assert df.index.tolist() == ['Mean', 'Median', 'Standard Deviation']
    assert df.columns.tolist() == ['Array1', 'Array2']

    assert np.allclose(df.loc['Mean', 'Array1'], np.mean(np.random.rand(array_length)))
    assert np.allclose(df.loc['Median', 'Array1'], np.median(np.random.rand(array_length)))
    assert np.allclose(df.loc['Standard Deviation', 'Array1'], np.std(np.random.rand(array_length)))

    assert np.allclose(df.loc['Mean', 'Array2'], np.mean(np.random.rand(array_length)))
    assert np.allclose(df.loc['Median', 'Array2'], np.median(np.random.rand(array_length)))
    assert np.allclose(df.loc['Standard Deviation', 'Array2'], np.std(np.random.rand(array_length)))