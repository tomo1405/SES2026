python
import pytest
from src_0036 import task_func

def test_task_func():
    df = {'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6], 'C': [3, 4, 5, 6, 7]}
    df = pd.DataFrame(df)
    target_values = [1, 3, 4]
    result_df, result_ax = task_func(df, target_values)
    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(result_ax, matplotlib.axes._subplots.Axes)
    assert result_df.shape == (5, 3)
    assert result_ax.get_xlabel() == 'Value'
    assert result_ax.get_ylabel() == 'Density'
    assert result_ax.get_title() == 'Density Plot of Selected Values'
    assert result_ax.get_legend().get_texts()[0].get_text() == 'A'
    assert result_ax.get_legend().get_texts()[1].get_text() == 'B'
    assert result_ax.get_legend().get_texts()[2].get_text() == 'C'