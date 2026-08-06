import matplotlib
import numpy as np
import pandas as pd
from src_0574 import task_func


def test_task_func():
    array_length = 100
    df, ax = task_func(array_length)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

    assert len(df) == 2
    assert len(df.columns) == 3
    assert len(df.index) == 3

    assert np.allclose(df['Array1'][0], np.mean(np.random.rand(array_length)))
    assert np.allclose(df['Array1'][1], np.median(np.random.rand(array_length)))
    assert np.allclose(df['Array1'][2], np.std(np.random.rand(array_length)))

    assert np.allclose(df['Array2'][0], np.mean(np.random.rand(array_length)))
    assert np.allclose(df['Array2'][1], np.median(np.random.rand(array_length)))
    assert np.allclose(df['Array2'][2], np.std(np.random.rand(array_length)))

    assert np.allclose(df.index, ['Mean', 'Median', 'Standard Deviation'])

    assert ax.get_xlabel() == 'Statistics'
    assert ax.get_ylabel() == 'Values'
    assert ax.get_title() == 'Statistics of Arrays'

    assert ax.get_xticks() == ['Array1', 'Array2']
    assert ax.get_yticks() == [0, 0.5, 1]

    assert ax.get_xticklabels() == ['Array1', 'Array2']
    assert ax.get_yticklabels() == ['0', '0.5', '1']