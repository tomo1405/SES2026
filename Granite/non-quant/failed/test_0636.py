import pytest
from src_0636 import task_func

def test_task_func():
    text = "This is a sample text. This is another sample text."
    matrix_df, ax = task_func(text)
    assert isinstance(matrix_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert matrix_df.shape == (len(matrix_df.columns), len(matrix_df.index))
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''

def test_task_func_empty_text():
    text = "This is a sample text. This is another sample text. This is a stopword. This is another stopword."
    matrix_df, ax = task_func(text)
    assert matrix_df.empty
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''

def test_task_func_n():
    text = "This is a sample text. This is another sample text."
    matrix_df_2, ax_2 = task_func(text, n=2)
    matrix_df_3, ax_3 = task_func(text, n=3)
    assert matrix_df_2.shape != matrix_df_3.shape
    assert ax_2.get_xlabel() != ax_3.get_xlabel()
    assert ax_2.get_ylabel() != ax_3.get_ylabel()