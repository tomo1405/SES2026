import pandas as pd
import pytest
from scipy.stats import chi2_contingency
from src_0885 import task_func

@pytest.mark.parametrize("df, columns, larger, equal, expected", [
    (pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}), ['A', 'B', 'C'], 50, 900, 0.0),
    (pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]}), ['A', 'B', 'C'], 50, 900, 0.0),
    (pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}), ['D', 'E', 'F'], 50, 900, ValueError),
    (pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}), ['A', 'B', 'C'], 50, 900, ValueError),
    (pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}), ['A', 'B', 'C'], 50, 900, ValueError),
])
def test_task_func(df, columns, larger, equal, expected):
    with pytest.raises(expected):
        result = task_func(df, columns, larger, equal)