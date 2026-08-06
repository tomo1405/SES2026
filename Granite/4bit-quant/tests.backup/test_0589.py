import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src_0589 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert 'X' in df.columns and 'Y' in df.columns
    assert df.shape == (SIZE, 2)

def test_task_func_scatterplot():
    df = task_func()
    assert len(plt.get_fignums()) == 1
    assert len(plt.get_current_fig_manager().toolbar.tools) == 6