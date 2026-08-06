import pytest
from src_0036 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, ax = task_func(df, target_values=[1, 3, 4])
    assert df.equals(pd.DataFrame({'A': [1, 0, 3], 'B': [0, 0, 0]}))
    assert ax.get_legend().get_texts() == ['A', 'B']
    assert ax.get_legend().get_lines() == [plt.Line2D([0], [0], color='red'), plt.Line2D([0], [0], color='blue')]