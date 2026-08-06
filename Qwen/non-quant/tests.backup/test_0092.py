import pytest
from src_0092 import task_func
import pandas as pd
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

def test_task_func_columns_exist():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result, ax = task_func(data, 'A', 'B')
    assert isinstance(result, tuple)
    assert len(result) == 5
    plt.close(ax.figure)

def test_task_func_columns_do_not_exist():
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(data, 'A', 'C')

def test_task_func_correct_regression():
    data = pd.DataFrame({
        'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 6, 8, 10]
    })
    result, ax = task_func(data, 'X', 'Y')
    slope, intercept, r_value, p_value, std_err = result
    assert np.isclose(slope, 2.0)
    assert np.isclose(intercept, 0.0)
    assert np.isclose(r_value, 1.0)
    plt.close(ax.figure)

def test_task_func_plot_correctness():
    data = pd.DataFrame({
        'X': [1, 2, 3, 4, 5],
        'Y': [2, 4, 6, 8, 10]
    })
    _, ax = task_func(data, 'X', 'Y')
    buf = BytesIO()
    ax.figure.savefig(buf, format='png')
    buf.seek(0)
    plt.close(ax.figure)
    # This is a basic check to ensure the plot was created
    assert buf.getbuffer().nbytes > 0

def test_task_func_empty_dataframe():
    data = pd.DataFrame(columns=['A', 'B'])
    with pytest.raises(ValueError):
        task_func(data, 'A', 'B')