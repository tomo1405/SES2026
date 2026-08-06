import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0252 import task_func

def test_task_func():
    data = pd.DataFrame({'Job': ['Developer', 'Data Scientist', 'Data Scientist', 'Developer', 'Product Manager']})
    fig = task_func(data)
    assert isinstance(fig, plt.Figure)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func('invalid input')