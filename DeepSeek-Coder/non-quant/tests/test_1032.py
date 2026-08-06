import pytest
from src_1032 import task_func

def test_task_func():
    result = task_func(n_rows=10)
    assert isinstance(result, plt.Axes)
    assert result.get_title() == "Top 30 Frequencies of Random 3-Letter Strings"