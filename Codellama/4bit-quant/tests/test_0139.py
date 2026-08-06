import matplotlib
import pandas as pd
import pytest
from src_0139 import task_func


def test_task_func():
    df = pd.DataFrame({'Letters': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']})
    ax = task_func(df)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == 'Letter Frequency'
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (0, 26)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_xticks() == np.arange(0, 26)
    assert ax.get_yticks() == np.arange(0, 1)
    assert ax.get_xticklabels() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    assert ax.get_yticklabels() == ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
    plt.close(ax.figure)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'Numbers': [1, 2, 3, 4, 5]}))