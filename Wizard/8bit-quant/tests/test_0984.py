python
import pytest
from src_0984 import task_func

def test_task_func_empty_df():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_task_func_non_numeric_df():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    with pytest.raises(TypeError):
        task_func(df)

def test_task_func_valid_df():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)