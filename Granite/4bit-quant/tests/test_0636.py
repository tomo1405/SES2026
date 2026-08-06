import matplotlib.pyplot as plt
import pandas as pd
from src_0636 import task_func


def test_task_func():
    text = "This is a sample text. This is another sample text."
    matrix_df, ax = task_func(text)
    assert isinstance(matrix_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_text():
    text = ""
    matrix_df, ax = task_func(text)
    assert matrix_df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_n_value():
    text = "This is a sample text. This is another sample text."
    n = 3
    matrix_df, ax = task_func(text, n)
    assert matrix_df.shape == (len(matrix_df.columns), len(matrix_df.index))