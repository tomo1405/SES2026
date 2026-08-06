import pytest
from src_0478 import task_func

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame), "The returned object is not a DataFrame."
    assert len(df) > 0, "The DataFrame is empty."
    assert "x" in df.columns, "The DataFrame does not contain the 'x' column."
    assert "y" in df.columns, "The DataFrame does not contain the 'y' column."
    assert "category" in df.columns, "The DataFrame does not contain the 'category' column."
    assert len(df) == 100, "The DataFrame does not have the expected number of rows."

    assert ax is not None, "The plot axes object is None."
    assert plt.gca() == ax, "The plot axes do not match the expected axes object."