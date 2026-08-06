import pandas as pd
import pytest
import seaborn as sns
from src_0984 import task_func


def test_task_func():
    # Test 1: Empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test 2: Non-numeric DataFrame
    df = pd.DataFrame({"A": ["a", "b", "c"], "B": [1, 2, 3]})
    with pytest.raises(TypeError):
        task_func(df)

    # Test 3: Valid DataFrame
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.PairGrid)

if __name__ == "__main__":
    pytest.main()