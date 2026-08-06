python
import pytest
from src_0984 import task_func

def test_task_func():
    # Test case 1: Empty DataFrame
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test case 2: Non-numeric DataFrame
    with pytest.raises(TypeError):
        task_func(pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]}))

    # Test case 3: Valid DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.PairGrid)