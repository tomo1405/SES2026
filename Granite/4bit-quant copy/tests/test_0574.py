import pytest
from src_0574 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, pd.plotting.dereference.BarPlot)
    assert df.index.tolist() == ['Mean', 'Median', 'Standard Deviation']
    assert df.columns.tolist() == ['Array1', 'Array2']
    assert df.loc['Mean', 'Array1'] == pytest.approx(np.mean(np.random.rand(100)))
    assert df.loc['Median', 'Array1'] == pytest.approx(np.median(np.random.rand(100)))
    assert df.loc['Standard Deviation', 'Array1'] == pytest.approx(np.std(np.random.rand(100)))
    assert df.loc['Mean', 'Array2'] == pytest.approx(np.mean(np.random.rand(100)))
    assert df.loc['Median', 'Array2'] == pytest.approx(np.median(np.random.rand(100)))
    assert df.loc['Standard Deviation', 'Array2'] == pytest.approx(np.std(np.random.rand(100)))