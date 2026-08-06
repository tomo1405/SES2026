import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0111 import task_func

@pytest.mark.parametrize("df, expected_exception", [
    (pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Sales': [10, 20, 30]}), None),
    (pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Sales': [10, 20, 30]}), ValueError),
    (pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Sales': [10, 20, 30]}), ValueError),
    (pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Sales': [10, 20, 30]}), None),
])
def test_task_func(df, expected_exception):
    if expected_exception is None:
        try:
            ax = task_func(df)
            assert isinstance(ax, plt.Axes)
        except Exception as e:
            pytest.fail(f"Unexpected exception: {e}")
    else:
        with pytest.raises(expected_exception):
            task_func(df)