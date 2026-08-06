import pytest
from src_0516 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    array = [["a", "b", "c", "d", "e"], ["1", "2", "3", "4", "5"]]
    expected_df = pd.DataFrame(array, columns=["A", "B", "C", "D", "E"])
    expected_heatmap = sns.heatmap(expected_df.corr(), annot=True)

    df, heatmap = task_func(array)

    assert df.equals(expected_df)
    assert heatmap == expected_heatmap

def test_task_func_with_invalid_input():
    array = [["a", "b", "c"], ["1", "2", "3", "4", "5"]]
    with pytest.raises(ValueError) as exc_info:
        task_func(array)
    assert "array must be non-empty and all sublists must have a length of 5." in str(exc_info.value)